from point import Point

class Circle:
    def __init__(self, center=Point(), radius=0):
        self.center = center
        self.radius = max(0, radius)

    @staticmethod
    def area(circle):
        return 3.14159 * circle.radius ** 2

    @staticmethod
    def move(circle, dx, dy):
        circle.center.move(dx, dy)
