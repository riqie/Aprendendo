from land import RectangularLand, SquareLand
from engineer import Engineer


myEngineer = Engineer("Joseph")
land1 = SquareLand(4)
land2 = RectangularLand(2, 4)

print("{} measured the perimeter: {} m.".format(myEngineer.name, myEngineer.measurePerimeter(land1)))

print("{} measured the area: {} m²".format(myEngineer.name, myEngineer.measureArea(land2)))