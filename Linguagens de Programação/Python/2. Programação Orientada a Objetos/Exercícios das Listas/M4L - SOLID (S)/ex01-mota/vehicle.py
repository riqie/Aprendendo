'''1. Escreva uma classe chamada Vehicle que possua campos para a velocidade atual em
km/h, a direção em graus dos pneus e o nome do proprietário. Crie métodos de
acesso e impressão para esta classe e faça um programa de teste.'''

class Vehicle:
    def __init__(self, speed=0 , degrees = 0, pilot_name = ""):
        self._speed = speed
        self._degrees = degrees
        self._pilot_name = pilot_name

    def set_speed(self, speed):
        if speed >= 0:
            self._speed= speed
        else:
            print("Speed must be greater than 0!")

    def set_degrees(self, degrees):
        if 0 <= degrees <= 360:
            self._degrees = degrees
        else:
            print("The car must be between 0 and 360 degrees!")

    def set_pilot(self, pilot):
        self._pilot_name = pilot

    def get_speed(self):
        return self._speed
    
    def get_degrees(self):
        return self._degrees
    
    def get_pilot_name(self):
        return self._pilot_name

    def get_infos(self):
        return f"Pilot Name: {self._pilot_name}\nActual Speed: {self._speed}km/h\nActual Degrees: {self._degrees}"
