import pytest
from bank import Bank, Database


class TestBankInit:
    def test_get_treasury_initialized(self):
        bank = Bank(100, Database())
        assert bank.get_treasury() == 100


class TestMoveFunds:
    def setup_method(self, method):
        self.bank = Bank(100, Database())

    def teardown_method(self, method):
        self.bank = None

    def test_move_funds_more_than_treasury_raises_error(self):
        with pytest.raises(Exception):
            assert self.bank.move_funds('salary', 200)

    def test_move_funds_updates_treasury(self):
        self.bank.move_funds('salary', 10)
        assert self.bank.get_treasury() == 90

    def test_move_funds_updates_account_balance(self):
        self.bank.move_funds('salary', 10)
        assert self.bank.get_balance('salary') == 10

