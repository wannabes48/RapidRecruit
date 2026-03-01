How the System Works
The project consists of four core components:

Résumé Parser: Reads PDF and DOCX files and extracts text

JD Parser: Analyses the job description to identify required skills

Keyword Extractor: Matches résumé content against a skills taxonomy

Scoring Engine: Ranks candidates using a weighted algorithm

Scoring Formula
Here’s the scoring formula we’ll use:

Total Score =
(Required Skills × 50%) +
(Preferred Skills × 25%) +
(Experience × 15%) +
(Keywords × 10%)
This approach ensures that essential skills carry more weight than secondary keywords.

How This Approach Helps Reduce Bias
This system evaluates résumés using predefined criteria instead of subjective judgment. Each résumé is scored based on the same set of required skills, preferred skills, experience indicators, and keywords.

Because all candidates are evaluated using the same weighted formula, personal factors such as writing style, formatting, or unconscious preferences don’t influence the ranking. The scoring logic focuses only on how closely a résumé matches the job requirements.

By normalising the evaluation process, the system promotes more consistent and objective screening, which helps reduce bias during the initial résumé review stage.

System Architecture
Input                    Processing                     Output
─────                    ──────────                     ──────

Résumés ──► Résumé Parser ──► Keyword Extractor ──┐
(PDF/DOCX)                                        │
                                                  ├──► Scoring Engine ──► Ranked Results
Job Description ──► JD Parser ────────────────────┘
(TXT/PDF)
The system follows a simple input–process–output flow.

Résumés and the job description are provided as inputs. The Résumé Parser extracts text from each résumé, while the JD Parser identifies required and preferred skills from the job description.

The extracted résumé text is then passed to the Keyword Extractor, which matches skills and keywords using a predefined taxonomy.

Finally, the Scoring Engine applies a weighted formula to calculate a score for each candidate and outputs a ranked list of résumés.

Project Structure
resume_screening_system/
├── app.py                    # Streamlit web interface
├── main.py                   # Command-line interface
├── parsers/
│   ├── resume_parser.py      # PDF/DOCX text extraction
│   └── jd_parser.py          # Job description parsing
├── extractors/
│   └── keyword_extractor.py  # Skills and experience extraction
├── matcher/
│   └── scorer.py             # Scoring algorithm
├── data/
│   ├── config.json           # Scoring weights
│   └── skills_taxonomy.json  # Skills database
└── requirements.txt          # Dependencies
The project is organised into clear, modular directories. Parsing logic, keyword extraction, and scoring are separated into their own folders, while configuration files and data are kept isolated. This structure keeps the codebase easy to navigate, maintain, and extend.
