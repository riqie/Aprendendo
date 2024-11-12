class Account:
    def __init__(self, balance):
        self._balance = balance

    def update(self, tax):
        self._balance += self._balance * tax

    def get_balance(self):
        return self._balance


