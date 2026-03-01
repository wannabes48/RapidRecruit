import streamlit as st
import os
from main import run_parallel_screening
from parsers.resume_parser import ResumeParser
from matcher.scorer import Scorer

jd_text = st.text_area(
    "Paste the job description here:",
    height=300
)

uploaded_files = st.file_uploader(
    "Upload resume files:",
    type=["pdf", "docx", "txt"],
    accept_multiple_files=True
)

if st.button("Screen Resumes", type="primary"):
    file_paths = []
    if not os.path.exists("input"): os.makedirs("input")
    
    for uploaded_file in uploaded_files:
        path = os.path.join("input", uploaded_file.name)
        with open(path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        file_paths.append(path)

    # 2. Trigger Parallel Processing
    with st.spinner(f"Processing on {os.cpu_count()} cores..."):
        results = run_parallel_screening(file_paths)
    
    # 3. Display Results
    for res in results:
        st.write(f"**{os.path.basename(res['file'])}**: {res['score']}% Match")