# Um dado material radioativo perde metade de sua massa a cada 50s. Dada a massa 
# inicial em gramas, fazer um algoritmo que determine o tempo necessário para que 
# essa massa seja menor que 0,5g

import time

def tempoMinimo(massa):

    while massa >= 0.5:
        print(f'Massa atual: {massa}kg')
        for i in range(50):
            time.sleep(0.25)
            massa /= 2
            print(i)

    return massa



def main():
    massa = int(input('Digite a massa do material radioativo: '))
    massaFinal = tempoMinimo(massa)
    print(massa)


main()
# arrumar o print da massa, melhorar o print do tempo.
