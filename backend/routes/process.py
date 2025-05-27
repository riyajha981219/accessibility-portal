from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from services.file_parser import parse_file
from services.summarizer import get_summary_from_gemini

router = APIRouter()

@router.post("/summarize-file")
async def summarize_file(file: UploadFile = File(...)):
    try:
        text = await parse_file(file)

        if text.strip().lower() == "unsupported file type":
            return {"error": "Unsupported file type"}

        summary_result = get_summary_from_gemini(text)
        return JSONResponse(
                status_code=200,
                content={
                    "status": "success",
                    "filename": file.filename,
                    "summary": summary_result
                }
            )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "status": "error",
                "message": str(e)
            }
        )