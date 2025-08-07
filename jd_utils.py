

import pdfplumber

def extract_jd_text_from_pdf(file):
    """
    Extract text from a Job Description PDF file (UploadedFile from Streamlit).
    """
    try:
        with pdfplumber.open(file) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text() or ""
            return text.strip()
    except Exception as e:
        print(f"[ERROR] Could not extract JD text: {e}")
        return ""
