'''1. Escreva uma classe chamada Vehicle que possua campos para a velocidade atual em
km/h, a direção em graus dos pneus e o nome do proprietário. Crie métodos de
acesso e impressão para esta classe e faça um programa de teste.'''

from new_vehicle import Vehicle

def main():
    Car = Vehicle()
    print("Vehicle information")

    Car.set_speed(200)
    Car.set_degrees(30)
    Car.set_pilot("Murilo")
    
    print("-"*80)
    print(Car.get_infos())

main()
