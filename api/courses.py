from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from typing import List

from api.utils.courses import get_course_by_id, get_courses, create_course
from pydantic_schema.course import Course, CreateCourse

from database.db_setup import get_db

routes = APIRouter()


@routes.get('/courses', response_model=List[Course])
def list_courses(db: Session = Depends(get_db)):
    return get_courses(db=db)


@routes.post('/courses', response_model=Course, status_code=201)
def create_new_course(course: CreateCourse, db: Session = Depends(get_db)):
    return create_course(db=db, course=course)


@routes.get('/courses/{course_id}')
def get_course(course_id: int, db: Session = Depends(get_db)):
    course_found = get_course_by_id(db, course_id)

    if course_found is None:
        raise HTTPException(404, 'Course not found')

    return course_found
