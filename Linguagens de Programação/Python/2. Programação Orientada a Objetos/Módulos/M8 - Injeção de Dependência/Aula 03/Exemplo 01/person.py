from smartphone import Smartphone  

class Person:
    def __init__(self, smartphone: Smartphone):
        self.__smartphone = smartphone

    def orderPizza(self):
        print('picking up the smartphone...')
        print('defining pizza flavor...')
        self.__smartphone.sendMessage('I want a pepperoni pizza')

    def study(self):
        print('sitting in the office...')
        self.__smartphone.watchYoutube()
        print('writing down the content...')