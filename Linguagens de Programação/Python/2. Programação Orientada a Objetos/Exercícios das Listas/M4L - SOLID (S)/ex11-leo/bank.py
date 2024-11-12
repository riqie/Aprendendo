from savingaccount import SavingsAccount
import random

class Bank:
    
    def __init__(self):
        self.users = {}

    def add(self, name,pin):
        id = random.randint(1000,9999)
        if name in self.users:
            return "User already exist."
        self.users[name] = {'pin':pin, 'conta': SavingsAccount(name, pin), 'ID':id}
        
    def remove(self, name,pin):
        if name in self.users:
            del self.users[name]
            return "User removed"
        else:
            return None
    
    def authenticator(self, name, pin, ):
        if name in self.users and self.users[name]['pin'] == pin:
            return  self.users[name]['conta']
        else:
            return "name do usuario ou pin incorretos."
        
    def getInfo(self,name, pin):
        return F"INFO:{name},{pin}"

    def __str__(self):
        return self.users
    
    def mostrarConta(self):
        print("Dados bancários:\n")
        for key, chave in self.users.items():
            id = chave['ID']
            print(f"Cliente: {key}, ID: {id}")
