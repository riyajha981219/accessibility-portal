import fitz
import docx
from fastapi import UploadFile

async def parse_file(file: UploadFile) -> str:
    ext = file.filename.split('.')[-1].lower()
    content = await file.read()

    if ext == 'pdf':
        with open("temp.pdf", "wb") as f:
            f.write(content)
        doc = fitz.open("temp.pdf")
        return "\n".join(page.get_text() for page in doc)

    elif ext == 'docx':
        with open("temp.docx", "wb") as f:
            f.write(content)
        doc = docx.Document("temp.docx")
        return "\n".join(p.text for p in doc.paragraphs)

    elif ext == 'txt':
        return content.decode('utf-8')

    else:
        return "Unsupported file type"
