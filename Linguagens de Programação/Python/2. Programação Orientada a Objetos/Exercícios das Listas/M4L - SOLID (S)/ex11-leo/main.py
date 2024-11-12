from new_bank import Bank
from new_savingaccount import SavingsAccount



def main():
    bradesco = Bank()
    bradesco.add("Leonardo","ssss")
    account = bradesco.authenticator("Leonardo", 0000)#erro na autenticacao com senha diferente
    #---------------------------------------------------
    account.deposit(2000)
    account.withdraw(400)
    print(account.getBalance())
    print(account.getName())
    print(account.getPin())
    print(account.computeInterest())
    print(account.__str__()   )
    #---------------------------------------------------
    santander = Bank()
    santander.add("Henrique",0000)
    b = santander.authenticator("Henrique",0000)
    b.getName()
    b.deposit(500)
    print(b.computeInterest())
    b.__str__()
    santander.showAccount()
    bradesco.showAccount()

main()
