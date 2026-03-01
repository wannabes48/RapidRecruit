import json
import re
from pathlib import Path

class JDParser:
    def __init__(self, taxonomy_path='data/skills_taxonomy.json'):
        with open(taxonomy_path, 'r') as f:
            self.taxonomy = json.load(f)

    def parse_jd(self, jd_text: str):
        """
        Analyzes JD text to determine the most likely job category 
        and extracts key requirements.
        """
        cleaned_text = jd_text.lower()
        category_scores = {}

        # 1. Auto-Detect Category
        for category, data in self.taxonomy.items():
            score = 0
            # Combine all skills in this category to check density
            all_keywords = data.get('required', []) + data.get('preferred', []) + data.get('keywords', [])
            
            for word in all_keywords:
                if re.search(rf'\b{re.escape(word.lower())}\b', cleaned_text):
                    score += 1
            
            category_scores[category] = score

        # Pick the category with the highest keyword match
        detected_category = max(category_scores, key=category_scores.get)
        
        # If no keywords matched at all, default to a generic category or the first one
        if category_scores[detected_category] == 0:
            detected_category = list(self.taxonomy.keys())[0]

        return {
            "detected_category": detected_category,
            "confidence_score": category_scores[detected_category],
            "raw_text": jd_text
        }