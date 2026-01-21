from app.db.db import session_maker
from app.derbit_client import DerbitClient
from app.services.price_service import PriceService
from app.worker.celery_app import celery_app


@celery_app.task
def collect_price():
    client = DerbitClient()
    with session_maker() as session:
        service = PriceService(session, client)
        service.get_and_save_price("eth_usd")
        service.get_and_save_price("btc_usd")
