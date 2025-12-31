from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.routes import upload
from backend.services.sdlc_classifier import classify_into_sdlc
from backend.services.pdf_handler import extract_text_from_pdf
from backend.utils.file_utils import save_uploaded_file, generate_pdf_response

app = FastAPI(
    title="SMART AI SDLC",
    description="API for classifying project documents into SDLC phases using OpenAI",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload.router)
