
'''5. Escreva uma classe Point descrito por coordenadas reais x, y. Crie métodos get e set
e faça um programa de teste para a sua classe. A seguir, crie e teste os seguintes
métodos para a classe Ponto:
a. O método que recebe como parâmetros um deslocamento dx e outro dy para
movimentar o Ponto.
b. O método que retorna a distância entre este ponto e outro dado como
parâmetro.
Crie e teste um construtor para a classe Point, que inicialize x e y em 1, mas que
também possa receber valores dados.'''

from new_point import Point

def main():

    point = Point(3,4)

    point.set_x(4)
    point.set_y(6)

    print(point.get_coords())

    point.move(1,3)

    print(point.get_coords())

    print(point.distance(3,5))    

main()
