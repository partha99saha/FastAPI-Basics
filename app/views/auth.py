# app/views/auth.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/auth/login")
def login():
    return {"message": "Login endpoint"}

@router.post("/auth/register")
def register():
    return {"message": "Register endpoint"}
