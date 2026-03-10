import json
import re
import spacy

class AdvancedScorer:
    def __init__(self, config_path='data/config.json', taxonomy_path='data/skills_taxonomy.json'):
        self.config = self._load_json(config_path)
        self.taxonomy = self._load_json(taxonomy_path)
        self.weights = self.config.get("weights", {})
        
        try:
            self.nlp = spacy.load("en_core_web_md")
        except OSError:
            print("Warning: en_core_web_md not found. Defaulting to blank spacy model.")
            self.nlp = spacy.blank("en")

    def _load_json(self, path):
        with open(path, 'r') as f:
            return json.load(f)

    def _calculate_weighted_match(self, text, targets, weight_multiplier):
        """
        Calculates score based on presence + frequency normalization.
        """
        if not targets:
            return 0
        
        match_count = 0
        text_lower = text.lower()
        
        # We parse the document once if we can use vectors
        use_vectors = self.nlp.vocab.vectors.shape[0] > 0
        resume_doc = self.nlp(text_lower) if use_vectors else None
        
        for target_group in targets:
            # If taxonomy hasn't been updated to lists, wrap the string in a list
            if isinstance(target_group, str):
                target_group = [target_group]
                
            group_matched = False
            best_similarity_found = False
            
            # 1. Exact Match via Regex
            for skill in target_group:
                pattern = rf'\b{re.escape(skill.lower())}\b'
                matches = re.findall(pattern, text_lower)
                if matches:
                    # Logarithmic scale: cap duplicate value
                    match_count += 1 if len(matches) == 1 else 1.2 
                    group_matched = True
                    break
                    
            # 2. Semantic Match via Spacy (Fallback)
            if not group_matched and use_vectors:
                for skill in target_group:
                    skill_token = self.nlp(skill.lower())
                    if skill_token and skill_token.has_vector:
                        for token in resume_doc:
                            if token.has_vector and token.is_alpha and not token.is_stop:
                                similarity = token.similarity(skill_token)
                                if similarity > 0.8: # Threshold for similarity
                                    match_count += 0.8 # Give partial credit
                                    best_similarity_found = True
                                    break
                    if best_similarity_found:
                        break
                        
        score = (match_count / len(targets)) * weight_multiplier
        return min(score, weight_multiplier)

    def calculate_total_score(self, resume_text, category):
        if category not in self.taxonomy:
            raise ValueError(f"Category '{category}' not found in skills taxonomy.")
            
        cat_data = self.taxonomy[category]
        
        # 1. Essential Skills (Highest priority)
        req_weight = self.weights.get('required_skills', 0.5)
        r_score = self._calculate_weighted_match(
            resume_text, cat_data.get('required', []), req_weight
        )
        
        # 2. Preferred Skills (Bonus)
        pref_weight = self.weights.get('preferred_skills', 0.25)
        p_score = self._calculate_weighted_match(
            resume_text, cat_data.get('preferred', []), pref_weight
        )
        
        # 3. Experience Validation
        exp_weight = self.weights.get('experience', 0.15)
        exp_score = 0
        
        # Check for phrases like "3+ years" or "5 years"
        if re.search(r'(\d+)\+?\s*years?', resume_text.lower()):
            exp_score = exp_weight
        else:
            # Fallback to general keyword match
            exp_keywords = self.config.get('experience_keywords', [])
            exp_matches = 0
            for word in exp_keywords:
                if re.search(rf'\b{re.escape(word.lower())}\b', resume_text.lower()):
                    exp_matches += 1
            if exp_keywords and exp_matches > 0:
                exp_score = (exp_matches / len(exp_keywords)) * exp_weight
                exp_score = min(exp_score, exp_weight)
                
        # 4. General Keywords
        key_weight = self.weights.get('keywords', 0.1)
        k_score = self._calculate_weighted_match(
            resume_text, cat_data.get('keywords', []), key_weight
        )

        total = (r_score + p_score + exp_score + k_score) * 100
        return round(min(total, 100), 2)