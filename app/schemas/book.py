from pydantic import BaseModel

class BookBase(BaseModel):
    title: str
    author: str
    description: str

class BookCreate(BookBase):
    title: str
    description: str

class Book(BookBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
