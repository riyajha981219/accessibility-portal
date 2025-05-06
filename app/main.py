from fastapi import FastAPI
from app.routers import documents

app = FastAPI()

app.include_router(documents.router)