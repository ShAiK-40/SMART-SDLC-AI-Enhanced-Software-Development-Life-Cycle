from fastapi import APIRouter, UploadFile, File
from backend.services.pdf_handler import extract_text_from_pdf
from backend.services.sdlc_classifier import classify_into_sdlc
from backend.utils.file_utils import save_uploaded_file, generate_pdf_response

router = APIRouter()

@router.post("/analyze")
async def analyze_document(file: UploadFile = File(...)):
    try:
        # Save the uploaded file
        file_path = save_uploaded_file(file)

        # Extract text from PDF
        extracted_text = extract_text_from_pdf(file_path)
        if not extracted_text.strip():
            return {"error": "Empty or unreadable document."}

        # Classify content using OpenAI API
        classified_data = classify_into_sdlc(extracted_text)

        # Generate output PDF and return the path
        output_pdf_path = generate_pdf_response(classified_data["content"])

        return {"message": "Success", "pdf_path": output_pdf_path}
    
    except Exception as e:
        return {"error": str(e)}
