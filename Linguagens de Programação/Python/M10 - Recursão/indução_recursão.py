# definir uma função/solução para um caso base

# definir a função/solução para um caso geral

# Exemplo: 
'''
Calcular o fatorial de um numero inteiro não negativo (n).
Caso base: 0! = 1
Passo indutivo: n! = n . (n - 1)!
'''

# Solução:
'''
Se n = 0 então 0! = 1
Se n >= 1 então n! = n . (n - 1)!
'''

# Código:
# def fatorial(n):
#     if n == 0:
#         return 1
#     else:
#         aux = fatorial(n - 1)
#     return n * aux

def main():
    numero = -1
    while numero < 0:
        numero = int(input("Entre com um numero: "))
        if numero < 0 :
            print('\t Valor invalido, tente novamente.')

    print(numero, '! = ', fatorial(numero), sep='')

# main()

'''
Veja bem... o 'else' e o 'aux' no código são desnecessários:
'''

def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n - 1)

main()