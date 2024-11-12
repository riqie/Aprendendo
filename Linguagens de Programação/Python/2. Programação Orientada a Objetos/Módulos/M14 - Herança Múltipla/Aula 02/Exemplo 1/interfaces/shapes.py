from abc import ABC, abstractmethod


class ShapesInterface(ABC):

    @abstractmethod
    def getPerimeter(self):
        pass

    @abstractmethod
    def getArea(self):
        pass

    