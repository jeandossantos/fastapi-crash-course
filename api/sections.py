from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

routes = APIRouter()


@routes.get('/sections')
def get_sections():
    return []
