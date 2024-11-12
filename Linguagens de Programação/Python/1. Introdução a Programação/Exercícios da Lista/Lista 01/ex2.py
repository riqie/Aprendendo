# Faça um programa que leia um conjunto de números positivos, sendo o conjunto 
# destes números finalizado quando for digitado um número negativo. Ao final, imprima 
# o maior e o menor número lido e a média deles.

def criarLista():
    conjuntoPositivo = []

    while True:
        numeroAdd = input("Digite um número positivo: ")

        if numeroAdd.isalpha():
            print('Não inserir letras.')
            continue

        else:
            numeroAdd = int(numeroAdd)

            if numeroAdd < 0:
                return conjuntoPositivo

            else:
                conjuntoPositivo.append(numeroAdd)

def equacoes(lista):
    
    media = []
    maior = max(lista)
    menor = min(lista)

    media.append(maior)
    media.append(menor)

    return media, maior, menor

def main():
    print('\nO programa fará uma lista com números positivos da escolha do usuário. Ao final ele indicará o maior número, o menor e resolverá a média entre estes dois.\nOBS: Digite um número negativo para fechar lista.\n')

    lista = criarLista()

    if lista == []:
        return print('Sua lista está vazia.')
    
    media, maior, menor = equacoes(lista)
    
    print(f'\nA lista ficou:{lista}\nO maior número da lista:{maior}\nO menor número da lista:{menor}\nA média: {sum(media) / len(media)}')

    print('\nFim do programa.')

main()

#finalizado
