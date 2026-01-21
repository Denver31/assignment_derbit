from sqlalchemy import create_engine, NullPool
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession  # type: ignore
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from app.config import settings

DATABASE_URL = f"postgresql+psycopg2://{settings.DB_USER}:{settings.DB_PASS}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
TEST_DATABASE_URL = f"postgresql+psycopg2://{settings.DB_USER}:{settings.DB_PASS}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.TEST_DB_NAME}"

DATABASE_PARAMS = {}
TEST_DATABASE_PARAMS = {"poolclass": NullPool}


engine = create_engine(DATABASE_URL, **DATABASE_PARAMS)
test_engine = create_engine(TEST_DATABASE_URL, **TEST_DATABASE_PARAMS)

session_maker = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)

session_maker_test = sessionmaker(
    bind=test_engine,
    autocommit=False,
    autoflush=False,
)


class Base(DeclarativeBase):
    pass
