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


@router.post('/follow/{user_id}', status_code=status.HTTP_201_CREATED)
async def follow(user_id: int, db: db_dependency, user: auth_dependency):
    data = {'user_id': user_id, 'follower_id': user.get('id')}
    following_user = db.query(User).filter(User.id == user_id).first()
    already_followed = db.query(Followers).filter(Followers.user_id == user_id,
                                                  Followers.follower_id == user.get('id')).first()
    if user_id == user.get('id'):
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
    followed_users = db.query(Followers).filter(Followers.follower_id == user.get('id')).all()
    user_ids = [{"user_id": user.user_id} for user in followed_users]
    return user_ids


@router.get("/followers", status_code=status.HTTP_200_OK, response_model=None)
async def get_followers(user: auth_dependency, db: db_dependency):
    followed_users = db.query(Followers).filter(Followers.user_id == user.get('id')).all()
    user_ids = [{"user_id": user.follower_id} for user in followed_users]
    return user_ids
