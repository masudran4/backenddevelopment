from typing import Annotated

from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from auths.helper import get_user_by_token
SQLALCHEMY_DATABASE_URL = 'sqlite:///todo.db'

Base = declarative_base()
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def get_db():
    db = SessionLocal()
    try:
        print("Yielding db session")
        yield db
    finally:
        print("Closing db session")
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]
auth_dependency = Annotated[dict,Depends(get_user_by_token)]