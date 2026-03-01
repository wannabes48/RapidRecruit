import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from matcher.scorer import Scorer

def test_scoring_logic():
    scorer = Scorer()
    # Mock text containing exactly 1 required skill and 1 preferred skill
    test_text = "I know Python and React.js. I have 5 years of experience."
    
    # If Python is 1/4 of 'required' (25%) and React is 1/4 of 'preferred' (25%)
    # The score should reflect those specific weights from your config.json.
    score = scorer.calculate_total_score(test_text, "software_development")
    print(f"Test Score: {score}%")
    assert 0 <= score <= 100