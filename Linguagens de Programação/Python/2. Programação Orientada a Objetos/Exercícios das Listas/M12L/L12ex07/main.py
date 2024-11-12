'''
a. Crie uma classe Account com um método chamado update() que atualiza a conta de
acordo com a taxa percentual:

    class Account:
    
        # Bank account
        def update(self, tax):
            self._balance += self._balance * tax


b. Crie duas subclasses da classe Account: CurrentAccount e SavingsAccount. Ambas
terão o método update() reescrito: a CurrentAccount deve atualizar-se com o dobro
da taxa e a SavingsAccount deve atualizar-se com o triplo da taxa.
'''

from classes import CurrentAccount, SavingsAccount, Account


def main():
    print("\nO programa fará:\n - cria a classe account\n - cria duas subclasses da classe account\n - usa polimorfismo: passa o metodo update para as classes filhas\n - utiliza os metodos")

    originalAccount = Account(1000)

    acc1 = CurrentAccount(1000)
    acc2 = SavingsAccount(1000)

    print("\nUpdate da classe pai:")
    originalAccount.update(2)
    print(f"  Saldo da Account: {originalAccount.get_balance()}")  

    print("\nUpdate das classes filhas:")
    acc1.update(2)  # Atualiza com 10% (2 * 2)
    acc2.update(2)  # Atualiza com 15% (2 * 3)

    print(f"  Saldo da CurrentAccount: {acc1.get_balance()}")  
    print(f"  Saldo da SavingsAccount: {acc2.get_balance()}\n")  

main()