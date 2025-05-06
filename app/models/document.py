from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.models import Base

class Document(Base):
    __tablename__ = 'documents'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True)
    content = Column(Text)
    format_type = Column(String(50))
    language = Column(String(50))
    tags = Column(String(255))
    created_at = Column(DateTime)