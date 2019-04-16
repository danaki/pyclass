class Database:
    def __init__(self):
        self.reset()

    def update_balance(self, account, new_balance):
        self.__balances[account] = new_balance

    def query_balance(self, account):
        return self.__balances.get(account, None)

    def reset(self):
        self.__balances = {}


class Bank:
    def __init__(self, treasury, db):
        self.__treasury = treasury
        self.__db = db

    def move_funds(self, account, amount):
        assert amount > 0

        if amount > self.__treasury:
            raise Exception('Not enough funds in treasury')

        current_balance = self.__db.query_balance(account)
        if current_balance is None:
            current_balance = 0

        self.__db.update_balance(account, current_balance + amount)
        self.__treasury = self.__treasury - amount

    def get_balance(self, account):
        current_balance = self.__db.query_balance(account)
        if current_balance is None:
            raise Exception('No account: ' + account)

        return current_balance

    def get_treasury(self):
        return self.__treasury
