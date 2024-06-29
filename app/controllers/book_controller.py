from sqlalchemy.orm import Session
from app.models.book import Book
from app.schemas.book import BookCreate


def get_books(db: Session, skip: int = 0, limit: int = 10):
    try:
        return db.query(Book).offset(skip).limit(limit).all()
    except Exception as e:
        raise str(e)


def create_book(db: Session, book: BookCreate, user_id: int):
    try:
        db_book = Book(**book.dict(), owner_id=user_id)
        db.add(db_book)
        db.commit()
        db.refresh(db_book)
        return db_book
    except Exception as e:
        raise str(e)
