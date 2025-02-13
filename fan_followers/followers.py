from typing import List

from pydantic import BaseModel, Field
from fastapi import APIRouter, HTTPException, Path
from starlette import status
from database import engine, db_dependency, auth_dependency
from . import models
from .models import Followers
from auths.models import User

router = APIRouter()

models.Base.metadata.create_all(bind=engine)


class Username(BaseModel):
    username: str = Field(min_length=3, max_length=50)

@router.post('/follow', status_code=status.HTTP_201_CREATED)
async def follow(username: Username, db: db_dependency, user: auth_dependency):
    username = username.model_dump().get('username')
    following_user = db.query(User).filter(User.username == username).first()
    data = {"follower_username": user.get('username'), "following_username": username}
    already_followed = db.query(Followers).filter(Followers.follower_username == user.get('username'),
                                                  Followers.following_username == username).first()
    if username == user.get('username'):
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail='Can not follow yourself')
    if already_followed:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='User is already followed')
    if following_user:
        item = Followers(**data)
        db.add(item)
        db.commit()
        db.refresh(item)
        return item
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='"User not found with given ID"')


@router.get("/followed", status_code=status.HTTP_200_OK, response_model=None)
async def get_followed_users(user: auth_dependency, db: db_dependency):
    followed_users = db.query(Followers).filter(Followers.follower_username == user.get('username')).all()
    user_ids = [{"user_id": user.following_username} for user in followed_users]
    return user_ids


@router.get("/followers", status_code=status.HTTP_200_OK, response_model=None)
async def get_followers(user: auth_dependency, db: db_dependency):
    followed_users = db.query(Followers).filter(Followers.following_username == user.get('username')).all()
    user_ids = [{"username": user.follower_username} for user in followed_users]
    return user_ids
