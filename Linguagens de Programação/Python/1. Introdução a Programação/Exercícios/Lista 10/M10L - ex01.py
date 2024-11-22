'''
Escreva uma função que calcule o enésimo número de Fibonacci de forma recursiva, 
a partir de um valor fornecido pelo usuário. Além disso, crie também uma função 
iterativa do Fibonacci e compare a quantidade de somas e a de tempo de execução.

Sequência de Fibonacci(15 primeiros termos): 
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377 
'''

from time import time

def fibonacci_recursao(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_recursao(n - 2) + fibonacci_recursao(n - 1)

def fibonacci(n):
    f_1 = 0
    f_2 = 1

    if n == 1:
        return f_1
    elif n == 2:
        return f_2
    else:
        for c in range(3, n + 1):
            f_3 = f_1 + f_2
            f_1, f_2 = f_2, f_3

        return f_3

def main():

    print("\n\tENÉSIMO TERMO DA SEQUÊNCIA DE FIBONACCI\n")

    n = 39

    inicio = time()
    resultado = fibonacci_recursao(n)
    fim = time()

    tempo_execucao = fim - inicio

    print(f"{n}° termo(por recursão) = {resultado}")
    print(f"Tempo de execução(por recursão) = {tempo_execucao} segundos")

    
    inicio_2 = time()
    resultado_2 = fibonacci(n)
    fim_2 = time()

    print(f"\n{n}° termo = {resultado_2}")
    tempo_execucao_2 = fim_2 - inicio_2
    print(f"Tempo de execução = {tempo_execucao_2} segundos")
    
main()
