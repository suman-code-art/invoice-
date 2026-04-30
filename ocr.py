import pytesseract
from pdf2image import convert_from_path
import pdfplumber

# (Optional now, since PATH works — but safe to keep)
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\SAMA\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'


def extract_text_from_pdf(pdf_path):
    text = ""

    # Try direct extraction (fast)
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    # If empty → OCR fallback
    if not text.strip():
        print("Using OCR...")
        images = convert_from_path(pdf_path)
        for img in images:
            text += pytesseract.image_to_string(img)

    return text


# 🔥 TEST
if __name__ == "__main__":
    file = "invoice.pdf"   # 👈 put your file here

    text = extract_text_from_pdf(file)

    print("\n===== EXTRACTED TEXT =====\n")
    print(text)