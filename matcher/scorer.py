import json
import re

class Scorer:
    def __init__(self, config_path='data/config.json', taxonomy_path='data/skills_taxonomy.json'):
        self.config = self._load_json(config_path)
        self.taxonomy = self._load_json(taxonomy_path)
        self.weights = self.config.get("weights", {})

    def _load_json(self, path):
        with open(path, 'r') as f:
            return json.load(f)

    def _clean_text(self, text):
        """Basic normalization to improve matching accuracy."""
        return re.sub(r'[^\w\s]', '', text.lower())

    def _calculate_match_ratio(self, text, target_list):
        """Returns the percentage of target items found in the text."""
        if not target_list:
            return 0
        
        found_count = 0
        cleaned_text = self._clean_text(text)
        
        for item in target_list:
            # Using regex boundaries \b to avoid partial matches (e.g., 'git' matching 'digital')
            pattern = rf'\b{re.escape(item.lower())}\b'
            if re.search(pattern, cleaned_text):
                found_count += 1
        
        return found_count / len(target_list)

    def calculate_total_score(self, resume_text, category):
        """
        Applies the weighted formula:
        (Req * 0.50) + (Pref * 0.25) + (Exp * 0.15) + (Key * 0.10)
        """
        if category not in self.taxonomy:
            raise ValueError(f"Category '{category}' not found in skills taxonomy.")

        cat_data = self.taxonomy[category]
        
        # 1. Required Skills (50%)
        req_score = self._calculate_match_ratio(resume_text, cat_data.get('required', []))
        
        # 2. Preferred Skills (25%)
        pref_score = self._calculate_match_ratio(resume_text, cat_data.get('preferred', []))
        
        # 3. Experience Indicators (15%)
        # Matches against the generic experience keywords in config.json
        exp_score = self._calculate_match_ratio(resume_text, self.config.get('experience_keywords', []))
        
        # 4. General Keywords (10%)
        key_score = self._calculate_match_ratio(resume_text, cat_data.get('keywords', []))

        # Weighted Sum
        final_score = (
            (req_score * self.weights.get('required_skills', 0.5)) +
            (pref_score * self.weights.get('preferred_skills', 0.25)) +
            (exp_score * self.weights.get('experience', 0.15)) +
            (key_score * self.weights.get('keywords', 0.1))
        )

        return round(final_score * 100, 2)  # Returns score out of 100