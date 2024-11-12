class Person:
    def __init__(self, name, surname, age):
        if not self.__verifyName(name):
            print('Invalid name!')
        
        self.__name = name
        self.__surname = surname
        self.__age = age

    @staticmethod
    def verifyName(name):
        return len(name) >= 3 and ' ' not in name
