from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import process

app = FastAPI()

# Allow requests from frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # We can restrict this later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the file upload route
app.include_router(process.router)