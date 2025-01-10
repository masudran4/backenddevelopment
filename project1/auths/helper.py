import os
from datetime import timedelta, timezone, datetime
from typing import Annotated

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from jose import jwt

SECRET_KEY = os.environ.get('SECRET_KEY')
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

hasher = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return hasher.verify(plain_password, hashed_password)


def create_access_token(username: str, user_id: int, expires_in: timedelta):
    encode = {
        "sub": username,
        "id": user_id,
        "expires_in": (datetime.now(timezone.utc) + expires_in).timestamp()
    }
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


async def get_user_by_token(token: Annotated[str, Depends(oauth2_scheme)]):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    username: str = payload.get("sub")
    id = payload.get("id")
    if username is None:
        raise HTTPException(status_code=401, detail="Could not validate credentials")
    if id is None:
        raise HTTPException(status_code=401, detail="Could not validate credentials")
    return {"username": username, "id": id}
