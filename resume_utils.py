

import pdfplumber

def extract_resume_text(file):
    """
    Extract text from a single resume file (UploadedFile or file path).
    """
    try:
        with pdfplumber.open(file) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text() or ""
            return text.strip()
    except Exception as e:
        print(f"[ERROR] Failed to process file: {file} | {e}")
        return ""

def process_resumes_from_paths(uploaded_files):
    """
    Takes a list of Streamlit UploadedFile objects.
    Returns a list of dicts: [{filename, content}, ...]
    """
    parsed = []
    for file in uploaded_files:
        text = extract_resume_text(file)
        if text:
            parsed.append({
                "filename": file.name,
                "content": text
            })
    return parsed
