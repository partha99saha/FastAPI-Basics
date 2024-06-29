from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from app.controllers.auth_controller import get_password_hash
from fastapi import HTTPException
from app.logger import logger


def get_user(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def create_user(db: Session, user: UserCreate):
    try:
        hashed_password = get_password_hash(user.password)
        db_user = User(
            username=user.username,
            email=user.email,
            hashed_password=hashed_password,
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except Exception as e:
        logger.error("Error in  create_user", exc_info=True)
        raise str(e)
