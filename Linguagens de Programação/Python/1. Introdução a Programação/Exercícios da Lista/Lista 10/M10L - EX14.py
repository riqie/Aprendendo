"""
14. Defina uma função recursiva que recebe como argumento uma w de listas de
números inteiros w e devolve True se todas as listas em w verificam a propriedade de
mais de metade dos seus elementos serem 0 e False em caso contrário. Por exemplo,
no caso da w [[0,0,3,0],[0,5,0],[0,0,0]] a função deve devolver True pois em todas as
listas mais de metade dos elementos são 0.
"""

def zeros(w):
    if w == []:
        return True

    if w[0].count(0) < len(w[0]) / 2:
        return False
    
    return zeros(w[1:])

def main():
    print('\nO programa vai lera uma lista de listas, caso nestas listas a maioria dos elementos seja 0, retornará: True. Caso contrário retornará: False.')

    w = [[0,0,3,0],[0,5,0],[0,0,0]]
    print('\nLista Exemplo:', w, '\nResposta:',zeros(w))

    w = [[2,1,3,0],[0,5,1],[1,9,0]]
    print('\nLista Exemplo:', w, '\nResposta:',zeros(w))

    print('\nFim do programa.')

main()
