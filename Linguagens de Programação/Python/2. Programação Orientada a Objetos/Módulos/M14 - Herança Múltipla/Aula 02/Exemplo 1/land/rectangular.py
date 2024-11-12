from interfaces.shapes import ShapesInterface


class RectangularLand(ShapesInterface):
    def __init__(self, width, length):
        self.__width = width
        self.__length = length

    def getPerimeter(self):
        return self.__width * 2 + self.__length * 2
    
    def getArea(self):
        return self.__width * self.__length