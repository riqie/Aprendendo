'''6. Escreva uma classe Circle composta de um ponto para indicar o centro e o tamanho 
do raio, que não deve ser menor que zero. Utilize a classe Point criada anteriormente. 
Crie métodos get e set para testar sua classe. A seguir crie: 
a. Um método que retorne a área do círculo.
b. Um método move que movimente o centro do círculo (utilize o método move 
da classe ponto).
Crie e teste um construtor para a classe Circle com todos os valores zerados, mas 
que também possa receber valores dados'''
from point import Point

class Circle:
    def __init__(self, center=Point(), radius=0):
        self.center = center
        self.radius = max(0, radius)

    def area(self):
        return 3.14159 * self.radius ** 2

    def move(self, dx, dy):
        self.center.move(dx, dy)
