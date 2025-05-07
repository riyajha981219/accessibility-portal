from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import DATABASE_URL
from app.models import Base  # Import Base from the models directory
from sqlalchemy.orm import Session
from contextlib import contextmanager

# Create the engine and sessionmaker
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db  # This is where the request gets access to the database session
    finally:
        db.close()  # Make sure to close the session after the request is finished