def extract_skills(self, text: str) -> Set[str]:
    text_lower = text.lower()
    found_skills = set()

    for category, skills_dict in self.skills_taxonomy.items():
        for skill_name, variations in skills_dict.items():
            for variation in variations:
                # Prevent "Java" matching "JavaScript"
                pattern = r"\\b" + re.escape(variation) + r"\\b"
                if re.search(pattern, text_lower):
                    found_skills.add(skill_name)
                    break

    return found_skills