'''
Defina uma função recursiva que recebe como argumento uma lista de listas de
números inteiros w e devolve o número de elementos pares que existem nas
sublistas de w. Por exemplo, no caso da lista [[2,4,3,1],[3,5,7],[],[8,0,6]] a função deve
devolver 5
'''

def contar_pares(lista):
    if lista == []:  # Caso lista vazia
        return 0
    primeira = lista[0]  # Pega a primeira sublista
    soma = 0
    for i in primeira:
        if i % 2 == 0:
            soma += 1  # Conta os pares na sublista
    return soma + contar_pares(lista[1:]) 

def main():
    print("Somando números pares de uma lista de listas")
    lista = [[1,2,3],[4,5,6],[2,2,2]]
    print("=" *80)
    print(lista)
    print("="*80)
    print("A quantidade de números pares na lista de listas é:")
    print(contar_pares(lista))

main()
