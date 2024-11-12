'''3. Crie uma classe Account que representa uma conta bancária. A classe deve fornecer
um método chamado debit para retirar dinheiro da conta. Assegure que a quantia de
débito não exceda o saldo de Account. Se exceder, o saldo deve ser deixado
inalterado e o método deve imprimir uma mensagem que indica “Quantia de débito
excedeu o saldo da conta”. Teste a classe implementada e seus métodos.'''

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
