import whisper
import os
import tempfile
from fastapi import UploadFile
import moviepy

model = whisper.load_model("base")

async def transcribe_audio_file(file: UploadFile) -> str:
    suffix = file.filename.split('.')[-1]
    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{suffix}") as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    result = model.transcribe(tmp_path)
    os.remove(tmp_path)
    return result['text']


async def transcribe_video_file(file: UploadFile) -> str:
    suffix = file.filename.split('.')[-1]
    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{suffix}") as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    audio_path = tmp_path.replace(f".{suffix}", ".mp3")
    video = moviepy.editor.VideoFileClip(tmp_path)
    video.audio.write_audiofile(audio_path)

    result = model.transcribe(audio_path)

    os.remove(tmp_path)
    os.remove(audio_path)
    return result['text']
