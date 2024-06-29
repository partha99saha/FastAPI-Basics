from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    author: str
    description: str


class BookCreate(BookBase):
    title: str
    author: str
    description: str


class Book(BookBase):
    id: str
    owner_id: str

    class Config:
        orm_mode = True
