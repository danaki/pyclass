import pytest
from bank import Bank, Database
from pytest import fixture, raises

@fixture
def mocked_db(mocker):
    db = Database()
    mocker.spy(db, 'query_balance')

    return db

def test_move_funds_queries_balance(mocked_db):
    bank = Bank(100, mocked_db)
    bank.move_funds('salary', 10)

    assert mocked_db.query_balance.call_count == 1
