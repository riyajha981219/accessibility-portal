from pydantic import BaseModel
from datetime import datetime

class DocumentBase(BaseModel):
    title: str
    content: str
    format_type: str
    language: str
    tags: str

class DocumentOut(DocumentBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True