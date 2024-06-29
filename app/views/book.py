from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.book import Book, BookCreate
from app.controllers.book_controller import get_books, create_book
from app.db import get_db
from app.middleware.auth import get_current_user
from app.models.user import User

router = APIRouter()


@router.get("/getbooks", response_model=List[Book])
def read_books(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    books = get_books(db, skip=skip, limit=limit)
    return books


@router.post("/addbooks", response_model=Book)
def create_book_for_user(
    book: BookCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return create_book(db=db, book=book, user_id=current_user.id)
