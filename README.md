## 🛠 Developer Documentation </br>

Welcome! This section is for developers who want to contribute to **RapidRecruit**.</br>

### 🏗 Architecture Overview</br>

RapidRecruit uses a **Modular Pipe-and-Filter** architecture. Each component is isolated to ensure that changing the parsing logic (e.g., switching from `PyPDF2` to `pdfplumber`) does not affect the scoring engine.</br>

### 🚀 Performance Strategy: Multiprocessing</br>

To handle high-volume screening, the system utilizes Python's `multiprocessing.Pool`.</br>

* **The Challenge:** PDF parsing is CPU-intensive and can block the MainThread in Streamlit.</br>
* **The Solution:** We spawn a worker for every CPU core available. Each worker independently initializes its own `ResumeParser` and `Scorer` to avoid shared-state memory issues.</br>

### 🛠 Local Development Setup</br>

1. **Clone & Environment:**</br>
```bash
git clone https://github.com/wannabes48/RapidRecruit.git
cd RapidRecruit
python -m venv venv
source venv/bin/scripts/activate  # Windows: venv\Scripts\activate

```


2. **Install Dependencies:**</br>
```bash</br>
pip install -r requirements.txt

```


3. **Running Tests:**</br>
We use `pytest` for unit testing. Always run tests before pushing changes:</br>
```bash
python -m pytest tests/

```



---

### 📂 Core Module Responsibilities</br>

| Module         | Responsibility                                     | Key File               |</br>
| **Parsers**    | Converts binary files (PDF/DOCX) to clean strings. | `resume_parser.py`     |</br>
| **Extractors** | Uses Regex and Taxonomy to find entities in text.  | `keyword_extractor.py` |</br>
| **Matcher**    | Applies weighted math to extracted data.           | `scorer.py`            |</br>
| **Interface**  | Manages the Streamlit state and file buffers.      | `app.py`               |</br>

---</br>

### 🤝 How to Contribute</br>

We follow a standard **Feature Branch** workflow:</br>

1. **Fork the Repo** and create your branch: `git checkout -b feature/AmazingFeature`.</br>
2. **Update the Taxonomy:** If adding new industries, update `data/skills_taxonomy.json`.</br>
3. **Refine the Scorer:** If improving the algorithm, ensure the final score is always normalized between **0 and 100**.</br>
4. **Commit Changes:** Use descriptive messages (`git commit -m 'Add support for .rtf files'`).</br>
5. **Push & PR:** Push to the branch and open a **Pull Request**.</br>

### 📝 Coding Standards</br>

* **Type Hinting:** Use Python type hints (e.g., `def func(text: str) -> int:`) for all new functions.</br>
* **Error Handling:** Always wrap file I/O operations in `try-except` blocks to prevent the multiprocessing pool from crashing on a single corrupt PDF.</br>
* **Documentation:** Add docstrings to all classes and public methods.</br>
