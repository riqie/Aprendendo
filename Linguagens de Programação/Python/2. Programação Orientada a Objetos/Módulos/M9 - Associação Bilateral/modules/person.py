class Person:
    def __init__(self, name):
        self.__name = name
        self.__local = None

    def enterThePlace(self, local: any):
        local.turnOnLights()

    def inidicateTheAddress(self, local: any):
        print(local.getAddress())

    def introduceYourself(self):
        print('Hi, i am {}'.format(self.__name))

    def getLocal(self):
        return self.__local
    
    def setLocal(self, local: any):
        self.__local = local
