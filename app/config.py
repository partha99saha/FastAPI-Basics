import os

# Read environment variables with defaults
# SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
# DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///./app.db')

PORT = 8000
SECRET_KEY = "Secret@123!"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 300
SQLALCHEMY_DATABASE_URL = "sqlite:///./app.db"

config = {
    "PORT": PORT,
    "SECRET_KEY": SECRET_KEY,
    "ALGORITHM": ALGORITHM,
    "ACCESS_TOKEN_EXPIRE_MINUTES": ACCESS_TOKEN_EXPIRE_MINUTES,
    "SQLALCHEMY_DATABASE_URL": SQLALCHEMY_DATABASE_URL
    }
