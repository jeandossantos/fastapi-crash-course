from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

routes = APIRouter()


@routes.get('/courses')
def get_courses():
    return []
