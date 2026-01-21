from fastapi import APIRouter, Query, Depends
from sqlalchemy.orm import Session

from app.api.dependencies import get_db
from app.services.price_service import PriceService

router = APIRouter(
    prefix="/prices",
    tags=["prices"],
)


@router.get("/all")
async def get_all_prices(ticker: str, session: Session = Depends(get_db)):
    service = PriceService(session)
    return service.get_all_prices(ticker)


@router.get("/latest")
async def get_latest_price(ticker: str, session: Session = Depends(get_db)):
    service = PriceService(session)
    return service.get_latest_price(ticker)


@router.get("/by_date_range")
async def get_prices_by_time_range(ticker: str = Query(..., description="Ticker"),
                                   start_time: int = Query(..., description="Start time"),
                                   end_time: str = Query(..., description="End time"),
                                   session: Session = Depends(get_db)):
    service = PriceService(session)
    return service.get_price_by_time_range(ticker, start_time, end_time)
