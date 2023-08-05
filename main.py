from typing import List
from fastapi import FastAPI, Path
from pydantic import BaseModel
from api import users, courses, sections
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
