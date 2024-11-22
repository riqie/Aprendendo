"""
2. Usando algoritmos recursivos, escreva funções que:
a. Some dois números inteiros não negativos, apenas usando incrementos e
decrementos unitários.
b. Multiplique dois números inteiros positivos, x e y, usando apenas somas e
subtrações.
c. Some todos os inteiros positivos pares menores ou iguais a um valor inteiro n.

"""

def soma(x, y):
    if x + y == 0:
        return 0
    return 1 + soma(x-1, y)

def multiplicacao(x, y):
    if y < 1:
        return 0
    return x + multiplicacao(x, y-1)

def somapares(n):
    if n < 2:
        return 0
    if n % 2 != 0:
        return somapares(n - 1)
    return n + somapares(n - 2)

def main():
    print('\nO programa realizará diversas equações:')

    print('\nSoma de dois número inteiros não negativos:')
    a, b = 200, 50
    print('Exemplo: a = 200, b = 50')
    print(soma(a,b))

    print('\nMultplicação de dois números inteiros positivos:')
    c, d = 3, 4
    print('Exemplo: c = 3, d = 4')
    print(multiplicacao(c, d))

    print('\nSoma de todos os números pares até n:')
    n = 8
    print('Exemplo: n = 8')
    print(somapares(n))
    
    print('\nFim do programa')

main()


