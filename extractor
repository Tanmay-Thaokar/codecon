import fitz  # PyMuPDF
file_path="test_file.pdf"
def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    full_text = ""
    for page in doc:
        full_text += page.get_text()
    return full_text

#file_path="test_file.pdf"
#extracted_text = extract_text_from_pdf(file_path)
#print(extracted_text)
