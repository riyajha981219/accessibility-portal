from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.services.db import get_db
from app.models.document import Document
from app.schemas.document import DocumentOut, DocumentBase

router = APIRouter()

@router.get("/documents", response_model=List[DocumentOut])
def get_documents(db: Session = Depends(get_db)):
    # Query to fetch all documents from the database
    documents = db.query(Document).all()  # db.query() is now correct
    if not documents:
        raise HTTPException(status_code=404, detail="Documents not found")
    return documents

@router.get("/documents/{document_id}", response_model=DocumentOut)
def get_document(document_id: int, db: Session = Depends(get_db)):
    doc = db.query(Document).filter(Document.id == document_id).first()
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")
    return doc

@router.post("/documents/", response_model=DocumentBase)
def create_document(document: DocumentBase, db: Session = Depends(get_db)):
    db_document = Document(
        title=document.title,
        content=document.content,
        format_type=document.format_type,
        language=document.language,
        tags=document.tags
    )
    db.add(db_document)
    db.commit()
    db.refresh(db_document)
    return db_document