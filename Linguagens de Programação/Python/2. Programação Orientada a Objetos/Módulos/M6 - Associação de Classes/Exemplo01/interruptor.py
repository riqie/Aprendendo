class Interruptor:
    def __init__(self, room):
        self.__room = room

    def turnOn(self):
        print('lighting the {}...'.format(self.__room))

    def turnOff(self):
        print('turning off the {} light...'.format(self.__room))