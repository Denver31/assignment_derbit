from typing import Generator

from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.db import session_maker
from app.services.price_service import PriceService


def get_db() -> Generator[Session, None, None]:
    db = session_maker()
    try:
        yield db
    finally:
        db.close()
