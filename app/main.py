from fastapi import FastAPI, Request
from app.routers import documents
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder

app = FastAPI()

app.include_router(documents.router)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = exc.errors()
    first_error = errors[0] if errors else None

    if first_error:
        field = ".".join(str(loc) for loc in first_error.get("loc", []))
        return JSONResponse(
            status_code=422,
            content={"message": f"{field} field is missing or invalid"},
        )

    return JSONResponse(
        status_code=422,
        content={"message": "Invalid input"},
    )