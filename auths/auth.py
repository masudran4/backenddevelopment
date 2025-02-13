from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel, Field
from starlette import status

from database import engine, db_dependency
from . import models
from .models import User
from .helper import hasher, verify_password, create_access_token

router = APIRouter()
models.Base.metadata.create_all(bind=engine)


class UsersReq(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    password: str = Field(min_length=8, max_length=20)
    email: str = Field(min_length=3, max_length=20)
    role: str = Field(min_length=3, max_length=10)
    active: bool = Field(default=True)


@router.post('/create_user', status_code=status.HTTP_201_CREATED)
async def create_user(new_user: UsersReq, db: db_dependency):
    new_user = User(
        username=new_user.username,
        email=new_user.email,
        role=new_user.role,
        is_active=1 if new_user.active == 'true' else 0,
        hashed_password=hasher.hash(new_user.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"user_id": new_user.id}


@router.post('/token', status_code=status.HTTP_200_OK)
async def get_token(user_credentials: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency):
    user = db.query(User).filter(User.username == user_credentials.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Incorrect username or password')
    if not verify_password(user_credentials.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Incorrect username or password')
    return {"access_token": create_access_token(user.username, user.id, timedelta(minutes=30))}
