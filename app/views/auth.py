from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.auth import Token
from app.controllers.auth_controller import authenticate_user
from app.db import conn_db
from app.schemas.user import UserCreate, UserResponse, Login
from app.controllers.user_controller import create_user, get_user

router = APIRouter()


@router.post("/signup", response_model=UserResponse)
def signup(user: UserCreate, db: Session = Depends(conn_db)):
    db_user = get_user(db, user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    db_user = create_user(db, user)
    return db_user


@router.post("/login", response_model=Token)
def login_for_access_token(login_data: Login, db: Session = Depends(conn_db)):
    access_token = authenticate_user(db, login_data.username, login_data.password)
    return {"access_token": str(access_token), "token_type": "bearer"}


@router.get("/getuser/{username}", response_model=UserResponse)
def read_user(username: str, db: Session = Depends(conn_db)):
    db_user = get_user(db, username)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
