import time
from typing import Optional

from app.dao.prices_dao import PriceDAO
from app.derbit_client import DerbitClient


class PriceService:
    def __init__(self, session, client: Optional[DerbitClient] = None):
        self.client = client
        self.session = session

    def get_and_save_price(self, ticker):
        price = self.client.get_index_price(ticker)
        PriceDAO.add(self.session, ticker, price, int(time.time()))

    def get_all_prices(self, ticker):
        return PriceDAO.get_all_by_ticker(self.session, ticker)

    def get_latest_price(self, ticker):
        return PriceDAO.get_latest_by_ticker(self.session, ticker)

    def get_price_by_time_range(self, ticker, start_time, end_time):
        return PriceDAO.get_by_time_range(self.session, ticker, start_time, end_time)