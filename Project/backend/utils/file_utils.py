import os
from fastapi import UploadFile
from datetime import datetime
from fpdf import FPDF

UPLOAD_DIR = "data/uploads"
OUTPUT_DIR = "outputs"

# Ensure directories exist
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

def save_uploaded_file(file: UploadFile) -> str:
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"{timestamp}_{file.filename}"
    file_path = os.path.join(UPLOAD_DIR, filename)

    with open(file_path, "wb") as f:
        f.write(file.file.read())

    return file_path

def generate_pdf_response(classified_content: str) -> str:
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    output_file = os.path.join(OUTPUT_DIR, f"SmartSDLC_{timestamp}.pdf")

    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)

    for line in classified_content.split("\n"):
        pdf.multi_cell(0, 10, line)

    pdf.output(output_file)
    return output_file
