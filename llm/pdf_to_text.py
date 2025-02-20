import fitz  # PyMuPDF


def extract_text_from_pdf(pdf_path):
    # Open the PDF file
    document = fitz.open(pdf_path)
    text = ""
    # Iterate through each page
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text += page.get_text()
    return text


if __name__ == "__main__":
    pdf_path = "ADOR - Data/BankABC_TermSheet_Template.pdf"
    text = extract_text_from_pdf(pdf_path)
    print(text)
