'''4. Crie uma versão nova da classe Account com um método chamado displayAccount, 
que exiba o name e o balance de uma conta passada como parâmetro. Altere também 
o main para, ao invés de imprimir diretamente o name e o balance da conta, use o 
método displayAccount, passando a conta como parâmetro.'''
from account import Account

def main():

    account_1 = Account('Leo',3000 )
    account_1.debit(2000)
    account_1.add(500)

    account_1.displayAccount()

main()
