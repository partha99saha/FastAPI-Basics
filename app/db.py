from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import config

engine = create_engine(
    config.SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
create_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db() -> Session:  # type: ignore
    db = create_session()
    try:
        yield db
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()
