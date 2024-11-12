
class Account:
    def __init__(self, balance):
        self._balance = balance

    def debit(self, value):
        if value > self._balance:
            return "Insuficcient balance"
        self._balance -= value

    def add(self, value):
        self._balance += value

    def get_balance(self):
        return f"Current balance {self._balance}"
