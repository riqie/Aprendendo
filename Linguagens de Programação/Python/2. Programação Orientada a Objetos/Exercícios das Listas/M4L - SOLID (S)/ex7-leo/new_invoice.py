class Invoice:
    # o atributo privado nao tem como ser alterado fora da classe sem um metodo
    def __init__(self,n_invoice,description,quantity=0,price=0.0):
        if self.__verify(quantity,price):
            
            self._n_invoice = n_invoice
            self._description = description
            self.setQuantity(quantity)  
            self.setPrice(price)
        else:
            self.__indicateError()
            raise ValueError("Invalid quantity or price")
        
    def getN_invoice(self):
        return self._n_invoice
    
    def getDescription(self):
        return self._description
    
    def getQuantity(self):
        return self._quantity
    
    def getPrice(self):
        return self._price
    
    
    def setN_invoice(self, valor):
        self._n_invoice = valor
    
    def setDescription(self,new_description):
        self._description = new_description
    
    def setQuantity(self,quantity):
        self._quantity = self.__valueNonNegative(quantity)
    def setPrice(self,price):
        self._price = self.__valueNonNegative(price)
        
    def totalInvoice(self):
        return f"Total invoice:{self._quantity * self._price}"
    
    def __indicateError(self):
        print("Invalid data")
        
    def __verify(self, quantity, price):
        if isinstance(quantity, int) and quantity >= 0 and isinstance(price, (int, float)):
            return True
        return False
    def __valueNonNegative(self,value):
        if value < 0:
            return 0
        return value
        
            
        
