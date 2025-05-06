from fastapi import APIRouter

router = APIRouter()

@router.get("/documents")
def read_documents():
    return {"message": "Hello, accessible world!"}