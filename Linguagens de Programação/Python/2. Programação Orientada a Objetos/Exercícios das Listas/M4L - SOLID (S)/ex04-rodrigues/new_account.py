'''4. Crie uma versão nova da classe Account com um método chamado displayAccount, 
que exiba o name e o balance de uma conta passada como parâmetro. Altere também 
o main para, ao invés de imprimir diretamente o name e o balance da conta, use o 
método displayAccount, passando a conta como parâmetro.'''

class Account:
    def __init__(self, name, balance):
        self.balance = balance
        self.name = name

    def verify_value(self, amount):
        if self.balance < amount:
            return False
        return True

    def debit(self, amount):
        if self.verify_value(amount):
            self.balance -= amount
        else:
            print("Valor inválido.")
    
    def add(self, value):
        self.balance += value

    def displayAccount(self):
        print(f"Name: {self.name}, balance: {self.balance}")
