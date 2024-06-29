from sqlalchemy import Column, Integer, String, Boolean
from app.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    full_name = Column(String, nullable=True)

    @staticmethod
    def get_user_by_username(db, username: str):
        return db.query(User).filter(User.username == username).first()
