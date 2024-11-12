'''3. Crie uma classe Account que representa uma conta bancária. A classe deve fornecer
um método chamado debit para retirar dinheiro da conta. Assegure que a quantia de
débito não exceda o saldo de Account. Se exceder, o saldo deve ser deixado
inalterado e o método deve imprimir uma mensagem que indica “Quantia de débito
excedeu o saldo da conta”. Teste a classe implementada e seus métodos.'''

from account import Account

def main():   
    account_1 = Account(5000)

    print(account_1.get_balance())

    account_1.debit(2000)

    print(account_1.get_balance())

    account_1.add(500)

    print(account_1.get_balance())

main()

