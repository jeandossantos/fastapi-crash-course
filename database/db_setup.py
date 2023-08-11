from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:94198380@localhost:5430/fastapi_course"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={},
    future=True,

)

SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine, future=True)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ASYNC POSTGRES/SQLALCHEMY CONFIG
####################################
ASYNC_SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://postgres:94198380@localhost:5430/fastapi_course"

async_engine = create_async_engine(
    ASYNC_SQLALCHEMY_DATABASE_URL
)

AsyncSessionLocal = sessionmaker(
    async_engine, class_=AsyncSession, expire_on_commit=False
)


async def async_get_db():
    async with AsyncSessionLocal() as db:
        yield db
        await db.commit()
