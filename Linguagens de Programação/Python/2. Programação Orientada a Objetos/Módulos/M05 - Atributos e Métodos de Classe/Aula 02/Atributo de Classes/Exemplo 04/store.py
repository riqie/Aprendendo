class Store:
    tax = 1.03

    def __init__(self, adress):
        self.__address = adress

    def showAddress(self):
        print(self.__address)

    @classmethod
    def sell(cls):
        return 100 * cls.tax
        
    @classmethod
    def setTax(cls, newTax):
        cls.tax = newTax