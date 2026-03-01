🚀 RapidRecruit: High-Performance Résumé Screening</br>
RapidRecruit is a Python-based screening system designed to handle large volumes of applications using Multiprocessing.</br>
It automates the initial phase of recruitment by objectively ranking candidates against specific Job Descriptions (JD).</br>

🛠 How the System Works</br>
The project consists of four core components:</br>
-Résumé Parser: Leverages parallel processing to read PDF/DOCX files and extract raw text.</br>
-JD Parser: Analyzes the job description to identify mandatory vs. preferred skills.</br>
-Keyword Extractor: Cross-references résumé content against a curated skills taxonomy.</br>
-Scoring Engine: Ranks candidates using a weighted, multi-factor algorithm.</br>

📊 Scoring Logic & Bias Reduction</br>
To ensure objective evaluation, the system applies a consistent weighted formula to every candidate:</br>

$$Total Score = (R \times 0.50) + (P \times 0.25) + (E \times 0.15) + (K \times 0.10)$$</br>

Where:</br>
$R$ (Required Skills): 50% weight (The "Must-Haves").</br>
$P$ (Preferred Skills): 25% weight (The "Nice-to-Haves").</br>
$E$ (Experience): 15% weight (Years/Seniority indicators).</br>
$K$ (Keywords): 10% weight (General industry terminology).</br>

⚖️ Reducing Bias</br>
By normalizing the evaluation process, RapidRecruit removes subjective judgment from the initial screen. Factors like formatting, font choice, or name-based unconscious bias are ignored in favor of hard skill matching.

🏗 System Architecture</br>

graph LR</br>
    A[Résumés PDF/DOCX] --> B[Résumé Parser]</br>
    C[Job Description] --> D[JD Parser]</br>
    B --> E[Keyword Extractor]</br>
    D --> E</br>
    E --> F[Scoring Engine]</br>
    F --> G[Ranked Results/Dashboard]</br>

📂 Project Structure</br>

resume_screening_system/</br>
├── app.py                    # Streamlit web interface</br>
├── main.py                   # CLI for bulk processing</br>
├── parsers/</br>
│   ├── resume_parser.py      # PDF/DOCX text extraction (Multiprocessing)</br>
│   └── jd_parser.py          # Job description parsing</br>
├── extractors/</br>
│   └── keyword_extractor.py  # Skills and experience extraction</br>
├── matcher/</br>
│   └── scorer.py             # Scoring algorithm logic</br>
├── data/</br>
│   ├── config.json           # Adjustable scoring weights</br>
│   └── skills_taxonomy.json  # Skills database</br>
└── requirements.txt          # Dependencies (PyMuPDF, Spacy, etc.)</br>

⚡ Multiprocessing Advantage</br>
Unlike standard parsers, RapidRecruit utilizes Python's multiprocessing module to distribute the parsing workload across all available CPU cores.</br>
This allows the system to process hundreds of résumés in the time it usually takes to process ten.
