import easyocr
from PIL import Image
import fitz  # PyMuPDF
import os

reader = easyocr.Reader(['en'], gpu=False)


def extract_text_from_image(image_path):
    result = reader.readtext(image_path, detail=0)
    return " ".join(result)


def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    full_text = ""

    for page in doc:
        pix = page.get_pixmap()
        temp_image = "temp_page.png"
        pix.save(temp_image)

        text = extract_text_from_image(temp_image)
        full_text += text + "\n"

        os.remove(temp_image)

    return full_text


def extract_certificate_text(file_path):
    extension = file_path.split(".")[-1].lower()

    if extension in ["jpg", "jpeg", "png"]:
        return extract_text_from_image(file_path)

    elif extension == "pdf":
        return extract_text_from_pdf(file_path)

    else:
        raise ValueError("Unsupported file format")