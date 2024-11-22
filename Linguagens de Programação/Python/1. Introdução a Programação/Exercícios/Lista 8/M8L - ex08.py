'''
8. Escreva uma função (FparaC) que receba uma temperatura em graus F e retorne a 
temperatura em graus C, sendo: C = (5/9)(F - 32). A seguir, faça um programa que, em loop, leia um valor para F da entrada padrão e o imprima o valor de C correspondente, utilizando a função FparaC.
'''

def receber_F():
    F = 0

    while F != -460.0:
        #Verificar se a entrada é um float e se o float é válido(> -460)
        try:
            F = float(input("Temperatura em Fahrenheit(-460 para finalizar o programa): "))
            if F == -460.0:
                break
            elif F < -460:
                print("\nERRO! Informe um número real maior que -460")
                print(65*"-")
            else:
                celcius = FparaC(F)
                print(f"\n{F}°F = {celcius:.2f}°C")
                print(65*"-")
        except ValueError:
            print("\nERRO! Informe um número real maior que -460")
            print(65*"-")
        
    print("\nFim programa")

def FparaC(f):
    C = (5 / 9) * (f - 32)

    return C

def main():
    print(f"\t{33*"-"}")
    print("\tConversão Fahrenheit para Celcius")
    print(f"\t{33*"-"}\n")
    receber_F()

main()
