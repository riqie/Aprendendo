class SavingsAccount:
    """This class represent a saving account with name,pin and balance """

    RATE = 0.02
    def __init__(self,name,pin):
       self._balance = 0.0
       self._name = name
       self._pin = pin
    
    def deposit(self,amount):
        "Do deposit"
        self._balance += amount
    
    def withdraw(self,amount):
        """Do withdraw"""
        if amount < 0:
            return "Amount must be bigger than 0"
        elif self._balance < amount:
            return "Insufficient balance. "
        else:
            self._balance -= amount

    def getBalance(self):
        """Get Balance"""
        return self._balance
    
    def getName(self):
        """Get name"""
        return self._name
    
    def getPin(self):
        """"Get pin"""
        return self._pin
    
    def computeInterest(self):
        """Calculate,deposit and return interest"""
        self._interest = self._balance * SavingsAccount.RATE
        
        self.deposit(self._interest)
        return self._interest
    def __str__(self):
        return f"The account interest around: ${self._interest}"
    
