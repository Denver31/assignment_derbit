from contextlib import asynccontextmanager

from fastapi import FastAPI
from app.api import prices_router
from app.db.db import Base, engine
from app.scheduler import start_scheduler


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)

    scheduler = start_scheduler()
    yield
    scheduler.shutdown()

app = FastAPI(lifespan=lifespan)
app.include_router(prices_router.router)

