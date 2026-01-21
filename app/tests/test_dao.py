import time

from app.db.db import session_maker_test
from app.dao.prices_dao import PriceDAO


def test_dao_lastest_price():
    with session_maker_test() as session:
        new_price = PriceDAO.add(session,"btc_usd",1000,time.time())
        last_price = PriceDAO.get_latest_by_ticker(session,"btc_usd")
        assert new_price == last_price
        PriceDAO.add(session,"btc_usd",2000,time.time())
        last_price = PriceDAO.get_latest_by_ticker(session,"btc_usd")
        assert new_price != last_price


def test_dao_range_price():
    with session_maker_test() as session:
        save_time = time.time()
        new_price = PriceDAO.add(session,"btc_usd",1000, save_time)
        new_price2 = PriceDAO.add(session,"btc_usd",1000, save_time-10)
        range_price = PriceDAO.get_by_time_range(session,"btc_usd", save_time-1, save_time+1)
        assert new_price in range_price
        assert new_price2 not in range_price


def test_all_prices():
    with session_maker_test() as session:
        p1 = PriceDAO.add(session, "btc_usd", 1001, time.time())
        p2 = PriceDAO.add(session, "btc_usd", 1002, time.time())
        p3 = PriceDAO.add(session, "btc_usd", 1003, time.time())
        prices = PriceDAO.get_all_by_ticker(session, "btc_usd")
        assert p1 in prices
        assert p2 in prices
        assert p3 in prices
        assert len(prices) == 3

