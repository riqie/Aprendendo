class House:
    def __init__(self):
        self.__address = 'Av. Paulista, 100'

    def turnOnLights(self):
        print('Turning on the lights...')

    def getAddress(self):
        return self.__address