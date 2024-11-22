from .account import Account


class CurrentAccount(Account):
    def update(self, tax):
        super().update(tax * 2)


class SavingsAccount(Account):
    def update(self, tax):
        super().update(tax * 3)