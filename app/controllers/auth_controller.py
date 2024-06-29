from typing import Optional
from middleware.auth import create_access_token
from sqlalchemy.orm import Session
from app.models.user import User
from passlib.context import CryptContext
from app.schemas.auth import TokenData
from fastapi import HTTPException, status
from app.logger import logger

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify the plain password against the hashed password.
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """
    Return the hashed password.
    """
    return pwd_context.hash(password)


def authenticate_user(db: Session, username: str, password: str) -> Optional[TokenData]:
    """
    Authenticate a user by username and password.
    """
    try:
        if not username or not password:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        user = db.query(User).filter(User.username == username).first()
        if not user or not verify_password(password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )

        return create_access_token(
            data={"sub": user.username},
        )
    except Exception as e:
        logger.error("Error in  authenticate_user", exc_info=True)
        raise str(e)
