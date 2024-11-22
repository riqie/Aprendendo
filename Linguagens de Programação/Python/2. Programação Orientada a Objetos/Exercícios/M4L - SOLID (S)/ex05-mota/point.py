'''5. Escreva uma classe Point descrito por coordenadas reais x, y. Crie métodos get e set
e faça um programa de teste para a sua classe. A seguir, crie e teste os seguintes
métodos para a classe Ponto:
a. O método que recebe como parâmetros um deslocamento dx e outro dy para
movimentar o Ponto.
b. O método que retorna a distância entre este ponto e outro dado como
parâmetro.
Crie e teste um construtor para a classe Point, que inicialize x e y em 1, mas que
também possa receber valores dados.'''

class Point:
    def __init__(self, x=1, y=1):
        self._x = x
        self._y = y

    def set_x(self, coordx): 
        self._x = coordx 

    def set_y(self, coordy): 
        self._y = coordy

    def get_coords(self):
        return f'Position: ({self._x}, {self._y})'
    
    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y
    
    def move(self, dx, dy): 
        self._x = dx
        self._y = dy

    def distance(self, dx2, dy2):
        return f'Distance: {(self._x - dx2)**2 + (self._y - dy2)**2}'
