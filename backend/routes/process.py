from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from services.file_parser import parse_file
from services.summarizer import get_summary_from_gemini
from services.audio_parser import transcribe_audio_file, transcribe_video_file

router = APIRouter()

@router.post("/summarize-file")
async def summarize_file(file: UploadFile = File(...)):
    try:
        if ext in ["mp3", "wav", "m4a"]:
            text = await transcribe_audio_file(file)
        elif ext in ["mp4", "mov", "avi", "mkv"]:
            text = await transcribe_video_file(file)
        elif ext in ["pdf", "docx", "txt"]:
            text = await parse_file(file)
        else:
            raise HTTPException(status_code=415, detail="Unsupported format")

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

@router.post("/transcribe")
async def transcribe_file(file: UploadFile = File(...)):
    ext = file.filename.split('.')[-1].lower()

    if ext in ["mp3", "wav", "m4a"]:
        text = await transcribe_audio_file(file)
    elif ext in ["mp4", "mov", "avi", "mkv"]:
        text = await transcribe_video_file(file)
    else:
        raise HTTPException(status_code=415, detail="Unsupported audio/video format")

    return JSONResponse(status_code=200, content={"transcription": text})