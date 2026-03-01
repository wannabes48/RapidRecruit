import PyPDF2
from docx import Document
from pathlib import Path
from multiprocessing import Pool, cpu_count

class ResumeParser:
    def extract_text(self, file_path: str) -> str:
        path = Path(file_path)
        if path.suffix == '.pdf':
            return self._extract_pdf(path)
        elif path.suffix == '.docx':
            return self._extract_docx(path)
        return ""

    def _extract_pdf(self, file_path: Path) -> str:
        text = ""
        try:
            with open(file_path, "rb") as file:
                pdf_reader = PyPDF2.PdfReader(file)
                for page in pdf_reader.pages:
                    text += page.extract_text() + "\n"
        except Exception as e:
            print(f"Error reading PDF {file_path}: {e}")
        return text.strip()

    def _extract_docx(self, file_path: Path) -> str:
        try:
            doc = Document(file_path)
            return "\n".join(para.text for para in doc.paragraphs).strip()
        except Exception as e:
            print(f"Error reading DOCX {file_path}: {e}")
            return ""