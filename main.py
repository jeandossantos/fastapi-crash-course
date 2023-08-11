from fastapi import FastAPI

from api import users, courses, sections
from database.db_setup import engine
from database.models import user, course

user.Base.metadata.create_all(bind=engine)
course.Base.metadata.create_all(bind=engine)

app = FastAPI(
    # Create metadata for tags - fast api documentation
    title="Fast API Crash Course",
    description="A YouTube fast course created by Faraday Academy",
    version="0.0.1",
    contact={
        "Name": "Jean",
        "email": "jeanddg@hotmail.com"
    },
    license_info={
        "name": "MIT"
    }
)

app.include_router(users.routes)
app.include_router(sections.routes)
app.include_router(courses.routes)
