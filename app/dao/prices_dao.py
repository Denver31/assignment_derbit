from sqlalchemy import insert, select
from sqlalchemy.orm import Session

from app.db.prices_model import Price


class PriceDAO:
    model = Price

    @classmethod
    def add(cls, session: Session, ticker: str, price: float, timestamp: int) -> Price:
        stmt = (
            insert(cls.model)
            .values(
                ticker=ticker,
                price=price,
                timestamp=timestamp,
            )
            .returning(cls.model)
        )
        result = session.execute(stmt)
        obj = result.scalar_one()
        session.commit()
        return obj

    @classmethod
    def get_all_by_ticker(
            cls,
            session: Session,
            ticker: str,
    ) -> list[Price]:
        stmt = (
            select(cls.model)
            .where(cls.model.ticker == ticker)
            .order_by(cls.model.timestamp)
        )
        result = session.execute(stmt)
        return result.scalars().all()

    @classmethod
    def get_latest_by_ticker(
            cls,
            session: Session,
            ticker: str,
    ) -> Price | None:
        stmt = (
            select(cls.model)
            .where(cls.model.ticker == ticker)
            .order_by(cls.model.timestamp.desc())
            .limit(1)
        )
        result = session.execute(stmt)
        return result.scalar_one_or_none()

    @classmethod
    def get_by_time_range(
            cls,
            session: Session,
            ticker: str,
            start_time: int,
            end_time: int,
    ) -> list[Price]:
        stmt = (
            select(cls.model)
            .where(
                cls.model.ticker == ticker,
                cls.model.timestamp.between(start_time, end_time),
            )
            .order_by(cls.model.timestamp)
        )
        result = session.execute(stmt)
        return result.scalars().all()
