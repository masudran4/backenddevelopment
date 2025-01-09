from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = 'sqlite:///todo.db'

Base = declarative_base()
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})
Session = sessionmaker(bind=engine, autoflush=False, autocommit=False)
