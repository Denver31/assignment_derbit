from decimal import Decimal

import requests


class DerbitClient:
    BASE_URL = "https://www.deribit.com/api/v2/"

    def get_index_price(self, ticker: str) -> float:
        endpoint = "public/get_index_price"
        r = requests.get(self.BASE_URL + endpoint, params={"index_name": ticker})
        data = r.json()
        return Decimal(str(data['result']['index_price']))

