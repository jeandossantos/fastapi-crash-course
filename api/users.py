from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

routes = APIRouter()

users = []


class User(BaseModel):
    email: str
    is_active: bool
    bio: str | None = None


@routes.get('/users', response_model=List[User])
def list_user():
    return users


@routes.get('/users/{id}', response_model=User | None)
def get_user_by_id(id: int):
    if users:
        return users[0]
    else:
        return None


@routes.post('/users')
def create_user(user: User):
    users.append(user)
    return {"msg": "User created!"}
