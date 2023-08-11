from sqlalchemy.orm import Session

from database.models.course import Course
from pydantic_schema.course import CreateCourse


def get_courses(db: Session):
    return db.query(Course).all()


def get_courses_by_user(db: Session, user_id: int):
    return db.query(Course).filter(Course.user_id == user_id).all()


def get_course_by_id(db: Session, course_id: int):
    return db.query(Course).filter(Course.id == course_id).first()


def create_course(db: Session, course: CreateCourse):
    course = Course(
        title=course.title,
        description=course.description,
        user_id=course.user_id
    )

    db.add(course)
    db.commit()
    db.refresh(course)

    return course
