from sqlalchemy import Integer, String, Numeric, BigInteger, Index
from sqlalchemy.orm import Mapped, mapped_column

from app.db.db import Base


class Price(Base):
    __tablename__ = "price"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    ticker: Mapped[str] = mapped_column(
        String,
        nullable=False,
        index=True,
    )

    price: Mapped[float] = mapped_column(
        Numeric,
        nullable=False,
    )

    timestamp: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
        index=True,
    )

    __table_args__ = (
        Index(
            "idx_prices_ticker_timestamp",
            "ticker",
            "timestamp",
        ),
    )
