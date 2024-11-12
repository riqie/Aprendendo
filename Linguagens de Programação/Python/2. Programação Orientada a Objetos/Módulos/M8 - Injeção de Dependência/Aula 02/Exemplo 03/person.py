from typing import Type
from house import House

class Person:
    def __init__(self, name, local: Type[House]):
        self.__name = name
        self.__local = local

    def enterThePlace(self):
        self.__local.turnOnLights()

    def indicateTheAddress(self):
        print(self.__local.getAddress())

