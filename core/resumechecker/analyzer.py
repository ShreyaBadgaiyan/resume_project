import pdfplumber
import spacy

def extract_text_from_pdf(pdf_path):
    text=""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text+=page.extract_text() + "\n"
    return text.strip()       

API_KEY="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"

