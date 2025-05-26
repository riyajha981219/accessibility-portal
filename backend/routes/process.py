from fastapi import APIRouter, UploadFile, File
from services.file_parser import parse_file
from services.summarizer import get_summary_from_gemini

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    content = await parse_file(file)
    summary = get_summary_from_gemini(content)
    return {
        "filename": file.filename,
        "summary": summary
    }