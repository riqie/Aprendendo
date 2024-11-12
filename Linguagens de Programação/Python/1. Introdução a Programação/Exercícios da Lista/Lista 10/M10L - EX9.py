'''
# Usando algoritmos recursivos, escreva funções que:
# a. Defina uma função que recebe como argumento um número natural n e
# devolva a lista dos n primeiros quadrados perfeitos.
# b. Defina uma função que recebe como argumento um número natural n e
# devolva a lista dos quadrados perfeitos até n, por ordem decrescente.
'''

def quadradosPerfeitos(n):
    if n == 0:
        return []
    
    return quadradosPerfeitos(n-1) + [n*n]


def quadrados_perfeitos(n, i=1):
    if i * i > n:
        return []
    return quadrados_perfeitos(n, i + 1) + [i * i]


def main():
    print('\n1. O programa fará uma lista dos quadrados perfeitos até o número "n".\n2. Em seguida, fará uma lista descrescente dos quadrados perfeitos até "n" informado.')

    n1 = 8
    n2 = 50

    print('\nExemplo 1: n =', n1, '\n1.',quadradosPerfeitos(n1))
    print('\nExemplo 2: n =', n2, '\n2.',quadrados_perfeitos(n2))
    
    print('\nFim do programa.')

main()
    
