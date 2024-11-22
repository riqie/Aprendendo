'''2. Escreva uma classe chamada Bicycle que possua campos para a velocidade, 
cadência dos pedais (número de rotações dos pedais por minuto), marcha atual e 
número de série. A velocidade e a cadência dos pedais não podem ser menores que 
zero, a marcha atual deve estar entre 1 e 18 e o número de série deve ser maior que 
1000. Crie constantes simbólicas e métodos de acesso e impressão que reflitam 
esses limites. Teste a classe implementada e seus métodos. A seguir, crie um método 
que calcule a velocidade relativa entre a bicicleta e outra dada como parâmetro. Teste 
o seu novo método.
'''

from new_bicycle import Bicycle

def main():
    b1 = Bicycle(20, 60, 5, 2000)
    b2 = Bicycle(15, 50, 4, 3000)
    b1.print_info(b1)
    b2.print_info(b2)
    print("Relative Speed:", b1.relative_speed(b2))
    
main()
