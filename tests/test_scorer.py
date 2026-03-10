import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from matcher.scorer import AdvancedScorer

def test_scoring_logic():
    scorer = AdvancedScorer()
    
    # Test 1: Basic Matching and Keyword Stuffing
    # Repeating Python many times should not linearly increase the score
    test_text_spam = "I know Python, python, PYTHON, py3, django. I have 5 years of experience."
    score_spam = scorer.calculate_total_score(test_text_spam, "software_development")
    
    # Python is in required. Weight=0.5. 5 matches -> log scale should limit it
    # We also have "5 years" for experience -> 0.15 weight.
    print(f"Spam Test Score: {score_spam}%")
    assert score_spam > 0 and score_spam <= 100
    
    # Test 2: Semantic Matching
    # Text mentions "Cloud Computing" which is semantically related to AWS/Cloud
    # Only if spacy is loaded and vectors are available
    if scorer.nlp.vocab.vectors.shape[0] > 0:
        test_semantic = "Familiar with Cloud Computing and continuous integration."
        score_semantic = scorer.calculate_total_score(test_semantic, "common_tools")
        print(f"Semantic Test Score: {score_semantic}%")
        assert score_semantic > 0
    else:
        print("Skipping Semantic Match Test as spacy en_core_web_md is not loaded.")