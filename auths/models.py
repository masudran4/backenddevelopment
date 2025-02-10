from sqlalchemy import Column, Integer, String

from database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(20), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    hashed_password = Column(String(50), nullable=False)
    is_active = Column(Integer, nullable=False)
    role = Column(String(20), nullable=False)