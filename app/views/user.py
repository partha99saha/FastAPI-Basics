# app/views/user.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/custom_users_route/")
def custom_users_route():
    return {"message": "This is a custom users route"}
