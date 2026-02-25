"""
Resume Parser Module
Extracts raw text from PDF and DOC/DOCX files.
"""

import io
from PyPDF2 import PdfReader
from docx import Document


def extract_text_from_pdf(file_bytes: bytes) -> str:
    """Extract all text from a PDF file."""
    reader = PdfReader(io.BytesIO(file_bytes))
    pages = []
    for page in reader.pages:
        text = page.extract_text()
        if text:
            pages.append(text)
    return "\n".join(pages)


def extract_text_from_docx(file_bytes: bytes) -> str:
    """Extract all text from a DOCX file."""
    doc = Document(io.BytesIO(file_bytes))
    paragraphs = [p.text for p in doc.paragraphs if p.text.strip()]
    return "\n".join(paragraphs)


def parse_resume(file_bytes: bytes, filename: str) -> str:
    """
    Route to the correct parser based on file extension.
    Returns extracted raw text.
    """
    lower = filename.lower()
    if lower.endswith(".pdf"):
        return extract_text_from_pdf(file_bytes)
    elif lower.endswith(".docx"):
        return extract_text_from_docx(file_bytes)
    elif lower.endswith(".doc"):
        # python-docx can sometimes handle .doc; fallback message otherwise
        try:
            return extract_text_from_docx(file_bytes)
        except Exception:
            raise ValueError(
                "Legacy .doc format is not fully supported. Please convert to .docx or .pdf."
            )
    else:
        raise ValueError(f"Unsupported file format: {filename}")
