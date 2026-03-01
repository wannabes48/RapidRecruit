from parsers.resume_parser import ResumeParser
from matcher.scorer import Scorer
from multiprocessing import Pool, cpu_count

def process_single_resume(file_path):
    """Worker function that runs in a separate process."""
    parser = ResumeParser()
    scorer = Scorer()
    
    text = parser.extract_text(file_path)
    # Assuming 'software_development' as default for now
    score = scorer.calculate_total_score(text, "software_development")
    
    return {"file": file_path, "score": score}

def run_parallel_screening(file_list):
    # Use 1 less than total cores to keep the OS stable
    num_cores = max(1, cpu_count() - 1)
    
    with Pool(processes=num_cores) as pool:
        results = pool.map(process_single_resume, file_list)
    
    # Sort by score descending
    return sorted(results, key=lambda x: x['score'], reverse=True)

def run_screening_process(jd_input, resume_paths):
    jd_parser = JDParser()
    analysis = jd_parser.parse_jd(jd_input)
    category = analysis['detected_category']
    
    print(f"--- Detected Job Category: {category.replace('_', ' ').title()} ---")
    
    # Now use your multiprocessing pool to score resumes against THIS category
    # (Using the logic we discussed in the previous step)
    results = run_parallel_screening(resume_paths, category)
    return results