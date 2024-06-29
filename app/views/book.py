# app/views/book.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/custom_books_route/")
def custom_books_route():
    return {"message": "This is a custom books route"}
