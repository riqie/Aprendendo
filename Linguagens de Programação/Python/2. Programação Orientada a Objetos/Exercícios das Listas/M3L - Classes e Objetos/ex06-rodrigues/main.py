'''6. Escreva uma classe Circle composta de um ponto para indicar o centro e o tamanho 
do raio, que não deve ser menor que zero. Utilize a classe Point criada anteriormente. 
Crie métodos get e set para testar sua classe. A seguir crie: 
3a. Um método que retorne a área do círculo.
b. Um método move que movimente o centro do círculo (utilize o método move 
da classe ponto).
Crie e teste um construtor para a classe Circle com todos os valores zerados, mas 
que também possa receber valores dados'''

from circle import Circle
from point import Point

def main():
    c = Circle(Point(1, 1), 5)
    print("Área do círculo:", c.area())
    c.move(2, 2)
    print(f"\nNovo centro do círculo: ({c.center.get_x()}, {c.center.get_y()})")

main()
