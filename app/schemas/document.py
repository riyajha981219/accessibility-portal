from pydantic import BaseModel, validator, Field
from datetime import datetime

class DocumentBase(BaseModel):
    title: str = Field(..., min_length=1)
    content: str = Field(..., min_length=1)
    format_type: str = Field(..., min_length=1)
    language: str = Field(..., min_length=1)
    tags: str = Field(..., min_length=1)

    @validator("format_type")
    def validate_format_type(cls, v):
        allowed = ["pdf", "docx", "txt"]
        if v.lower() not in allowed:
            raise ValueError(f"Unsupported format_type '{v}'. Must be one of {allowed}.")
        return v.lower()

class DocumentOut(DocumentBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True