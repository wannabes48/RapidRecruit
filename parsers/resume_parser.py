def _extract_pdf(self, file_path: Path) -> str:
    text = ""
    with open(file_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page in pdf_reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\\n"
    return text.strip()

def _extract_docx(self, file_path: Path) -> str:
    from docx import Document
    doc = Document(file_path)
    return "\\n".join(
        para.text for para in doc.paragraphs
    ).strip()