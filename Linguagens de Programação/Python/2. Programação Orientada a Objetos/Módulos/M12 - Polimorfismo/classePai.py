from abc import ABC, abstractmethod


class Pai:
    def apresentar(self):
        print('Apresentando a classe pai.')

    @abstractmethod
    def abstractMethod(self):
        pass