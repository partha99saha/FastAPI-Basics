from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.db import Base
import uuid


class Book(Base):
    __tablename__ = "books"

    id = Column(String, primary_key=True, index=True, default=str(uuid.uuid4()))
    title = Column(String, index=True)
    author = Column(String, nullable=True)
    owner_id = Column(String, nullable=True)
    description = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
