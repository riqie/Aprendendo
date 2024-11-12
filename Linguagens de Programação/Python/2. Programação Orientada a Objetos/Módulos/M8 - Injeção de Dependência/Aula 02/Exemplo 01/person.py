class Person:
    def __init__(self, name):
        self.__name = name

    def enterThePlace(self, local: any):
        local.turnOnLights()

    def indicateTheAddress(self, local: any):
        print(local.getAddress())

