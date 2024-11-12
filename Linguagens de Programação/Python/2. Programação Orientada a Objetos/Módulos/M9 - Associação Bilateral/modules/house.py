class House:
    def __init__(self):
        self.__address = 'Av. paulista, 100'
        self.__owner = None

    def turnOnLights(self):
        print('Turning on the lights')

    def getAddress(self):
        return self.__address
    
    def setOwner(self, owner: any):
        self.__owner = owner #dependency injection by setter

    def getOwner(self):
        return self.__owner