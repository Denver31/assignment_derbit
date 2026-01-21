import pytest

from app.db.db import test_engine, Base



@pytest.fixture(autouse=True)
def prepare_database():
    Base.metadata.drop_all(bind=test_engine)
    Base.metadata.create_all(bind=test_engine)
    yield
    Base.metadata.drop_all(bind=test_engine)