from typing import Type
from interruptor import Interruptor

class Person:
    def turningOnTheLight(self, interruptor: Type[Interruptor]):
        interruptor.turnOn()

    def turningOffTheLight(self, interruptor: Type[Interruptor]):
        interruptor.turnOff()

    def sleep(self):
        print('went to sleep... zzzz...')