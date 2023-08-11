from pydantic import BaseModel

from datetime import datetime


class CourseBase(BaseModel):
    title: str
    description: str
    user_id: int


class CreateCourse(CourseBase):
    pass


class Course(CourseBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config():
        from_attributes = True
