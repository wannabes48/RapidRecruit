🚀 RapidRecruit: High-Performance Résumé Screening</br>
RapidRecruit is a Python-based screening system designed to handle large volumes of applications using Multiprocessing. It automates the initial phase of recruitment by objectively ranking candidates against specific Job Descriptions (JD).

🛠 How the System Works</br>
The project consists of four core components:</br>
-Résumé Parser: Leverages parallel processing to read PDF/DOCX files and extract raw text.</br>
-JD Parser: Analyzes the job description to identify mandatory vs. preferred skills.</br>
-Keyword Extractor: Cross-references résumé content against a curated skills taxonomy.</br>
-Scoring Engine: Ranks candidates using a weighted, multi-factor algorithm.</br>

📊 Scoring Logic & Bias Reduction</br>
To ensure objective evaluation, the system applies a consistent weighted formula to every candidate:</br>
$$Total Score = (R \times 0.50) + (P \times 0.25) + (E \times 0.15) + (K \times 0.10)$$
Where:</br>
$R$ (Required Skills): 50% weight (The "Must-Haves").
$P$ (Preferred Skills): 25% weight (The "Nice-to-Haves").
$E$ (Experience): 15% weight (Years/Seniority indicators).
$K$ (Keywords): 10% weight (General industry terminology).

⚖️ Reducing Bias</br>
By normalizing the evaluation process, RapidRecruit removes subjective judgment from the initial screen. Factors like formatting, font choice, or name-based unconscious bias are ignored in favor of hard skill matching.

🏗 System Architecture</br>

graph LR</br>
    A[Résumés PDF/DOCX] --> B[Résumé Parser]
    C[Job Description] --> D[JD Parser]
    B --> E[Keyword Extractor]
    D --> E
    E --> F[Scoring Engine]
    F --> G[Ranked Results/Dashboard]

📂 Project Structure</br>

resume_screening_system/
├── app.py                    # Streamlit web interface
├── main.py                   # CLI for bulk processing
├── parsers/
│   ├── resume_parser.py      # PDF/DOCX text extraction (Multiprocessing)
│   └── jd_parser.py          # Job description parsing
├── extractors/
│   └── keyword_extractor.py  # Skills and experience extraction
├── matcher/
│   └── scorer.py             # Scoring algorithm logic
├── data/
│   ├── config.json           # Adjustable scoring weights
│   └── skills_taxonomy.json  # Skills database
└── requirements.txt          # Dependencies (PyMuPDF, Spacy, etc.)

⚡ Multiprocessing Advantage</br>
Unlike standard parsers, RapidRecruit utilizes Python's multiprocessing module to distribute the parsing workload across all available CPU cores. This allows the system to process hundreds of résumés in the time it usually takes to process ten.
