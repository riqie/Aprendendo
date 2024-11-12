"""
13. Defina uma função recursiva que recebe como argumento uma lista de listas de
números inteiros w e devolve True se alguma das listas em w tiver mais números
pares do que ímpares e False em caso contrário. Por exemplo, no caso da lista
[[2,4,3,1],[3,5,7],[8,1,6]] a função deve devolver True pois a lista [8,1,6] tem mais pares
que ímpares.

"""
def parimpar(w):
    if w == []:
        return False

    par = qtd_par(w[0])
    impar = qtd_impar(w[0])
    
    if par > impar:
        return True
    return parimpar(w[1:])

def qtd_par(w):
    if w == []:
        return 0

    if w[0] % 2 == 0:
        return 1 + qtd_par(w[1:])
    return qtd_par(w[1:])

def qtd_impar(w):
    if w == []:
        return 0

    if w[0] % 2 != 0:
        return 1 + qtd_impar(w[1:])
    return qtd_impar(w[1:])

def main():
    print('\nO programa vai ler uma lista de listas, caso exista mais números pares, em qualquer uma das listas, ele retornará: True, caso contrário retornará: False')

    w = [[2,4,3,1],[3,5,7],[8,1,6]]
    print('\nLista exemplo:', w,'\nResposta:', parimpar(w))

    w = [[2,0,3,1],[3,5,7],[9,1,6]]
    print('\nLista exemplo:', w,'\nResposta:', parimpar(w))

    print('\nFim do programa')

main()
