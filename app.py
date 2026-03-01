import streamlit as st

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
    st.success("Processing resumes...")