'''2. Escreva uma classe chamada Bicycle que possua campos para a velocidade, 
cadência dos pedais (número de rotações dos pedais por minuto), marcha atual e 
número de série. A velocidade e a cadência dos pedais não podem ser menores que 
zero, a marcha atual deve estar entre 1 e 18 e o número de série deve ser maior que 
1000. Crie constantes simbólicas e métodos de acesso e impressão que reflitam 
esses limites. Teste a classe implementada e seus métodos. A seguir, crie um método 
que calcule a velocidade relativa entre a bicicleta e outra dada como parâmetro. Teste 
o seu novo método.
'''

class Bicycle:
    MAX_GEAR = 18
    MIN_SERIAL_NUMBER = 1000

    def __init__(self, speed, pedal_cadence, current_gear, serial_number):
        self.speed = max(0, speed)
        self.pedal_cadence = max(0, pedal_cadence)
        self.current_gear = min(max(1, current_gear), self.MAX_GEAR)
        self.serial_number = max(serial_number, self.MIN_SERIAL_NUMBER)

    def relative_speed(self, other_bike):
        return abs(self.speed - other_bike.speed)

    @staticmethod
    def print_info(bicycle):
        print(f"Velocidade: {bicycle.speed} km/h, Cadência: {bicycle.pedal_cadence} rpm, Marcha: {bicycle.current_gear}, Nº de Série: {bicycle.serial_number}")
