'''4. Crie uma versão nova da classe Account com um método chamado displayAccount, 
que exiba o name e o balance de uma conta passada como parâmetro. Altere também 
o main para, ao invés de imprimir diretamente o name e o balance da conta, use o 
método displayAccount, passando a conta como parâmetro.'''

class Account:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def debit(self, value):
        if value > self._balance:
            return "Insuficcient balance"
        self._balance -= value

    def add(self, value):
        self._balance += value

    def displayAccount(self):
        print(f"Name: {self._name}, balance: {self._balance}")
