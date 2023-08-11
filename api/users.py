from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database.db_setup import get_db
from pydantic_schema.user import UserCreate, User
from .utils.users import create_user, get_user, get_user_by_email, get_users

routes = APIRouter()


@routes.get('/users', response_model=List[User])
def list_user(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users(db=db, skip=skip, limit=limit)

    return users


@routes.get('/users/{id}', response_model=User)
def get_user_by_id(id: int, db: Session = Depends(get_db)):
    user = get_user(db, id)

    if user is None:
        raise HTTPException(404, 'User not Found')

    return user


@routes.post('/users', status_code=201)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    user_already_exists = get_user_by_email(db, user.email)

    if user_already_exists:
        raise HTTPException(400, 'User already exists.')

    return create_user(db, user)
