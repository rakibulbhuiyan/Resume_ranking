import pdfplumber
import spacy

# using for extract text from pdf


def exrtract_text_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    
    return text.strip()

file_path = "cv_of_Rakibul_Hasan.pdf"
print(exrtract_text_pdf(file_path))