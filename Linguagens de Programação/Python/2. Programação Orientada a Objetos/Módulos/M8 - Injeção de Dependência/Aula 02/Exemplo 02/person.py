class Person:
    def __init__(self, name, local: any):
        self.__name = name
        self.__local = local

    def enterThePlace(self):
        self.__local.turnOnLights()

    def indicateTheAddress(self):
        print(self.__local.getAddress())

