from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from services.file_parser import parse_file
from services.summarizer import get_summary_from_gemini
from bs4 import BeautifulSoup
from pydantic import BaseModel
import requests

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

class URLRequest(BaseModel):
    url: str

@router.post("/summarize-url")
def summarize_url(data: URLRequest):
    print(data)
    try:
        response = requests.get(data.url, timeout=10)
        soup = BeautifulSoup(response.content, "html.parser")
        print(f"response: {response}")

        # Extract main article content
        text = ' '.join(p.get_text() for p in soup.find_all('p'))
        
        if not text:
            raise Exception("No content found")

        # Use your existing summarization logic here
        summary_result = get_summary_from_gemini(text)  # reuse your LLM function
        return JSONResponse(
                status_code=200,
                content={
                    "status": "success",
                    "filename": data.url,
                    "summary": summary_result
                }
            )
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to parse or summarize: {str(e)}")