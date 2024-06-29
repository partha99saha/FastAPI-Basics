from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str


class Login(BaseModel):
    username: str
    password: str


class UserCreate(UserBase):
    password: str


class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True
