from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from app.config import config

engine = create_engine(config["SQLALCHEMY_DATABASE_URL"], connect_args={"check_same_thread": False})
create_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def conn_db() -> Session:  # type: ignore
    db = create_session()
    try:
        yield db
    except Exception:
        db.rollback()
    finally:
        db.close()
