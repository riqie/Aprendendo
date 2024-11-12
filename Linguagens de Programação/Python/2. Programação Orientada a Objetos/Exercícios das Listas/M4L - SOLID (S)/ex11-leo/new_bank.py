from savingaccount import SavingsAccount
import random

class Bank:
    
    def __init__(self):
        self.users = {}

    def add(self, name,pin):
        self.__name = self.verify_name(name)
        self.__pin = self.verify_pin(pin)
        id = random.randint(1000,9999)
        self.creating_user(self.__name,id)
        
    def creating_user(self,name,id):
        if name in self.users:
            return "User already exist."
        self.users[self.__name] = {'pin':self.__pin, 'conta': SavingsAccount(self.__name, self.__pin), 'ID':id}
        
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
            return self.users[name]['conta']
        
    def getInfo(self,name, pin):
        return F"INFO:{name},{pin}"

    def __str__(self):
        return self.users
    
    def showAccount(self):
        print("Dados bancários:\n")
        for key, chave in self.users.items():
            id = chave['ID']
            print(f"Cliente: {key}, ID: {id}")
    
    def verify_name(self,name):
        if isinstance(name,str):
            return name
        return "Unusual name"
    def verify_pin(self,pin):
        if isinstance(pin,int):
            return pin
        return 0
