from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .db import Base, engine
from .views import auth as auth_view
from .views import book as book_view

Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS settings
origins = ["http://localhost", "http://localhost:8000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoint for Swagger UI "/docs"
# http://localhost:8000/docs

# Include routers from views
app.include_router(auth_view.router, prefix="/auth", tags=["auth"])
app.include_router(book_view.router, prefix="/books", tags=["books"])
