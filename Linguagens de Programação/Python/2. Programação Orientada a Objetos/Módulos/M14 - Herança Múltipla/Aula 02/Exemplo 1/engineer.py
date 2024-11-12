from typing import Type
from interfaces import ShapesInterface


class Engineer:
    def __init__(self, name):
        self.name = name

    def measurePerimeter(self, land: ShapesInterface):
        return land.getPerimeter()

    def measureArea(self, land: ShapesInterface):
        return land.getArea()

    