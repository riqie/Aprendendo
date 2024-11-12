'''
# Usando algoritmos recursivos, escreva funções que:
# a. Calcule o produtório de um número m, n vezes.
# b. Calcule a potência n de um número k.
# c. Some os dígitos de um número inteiro não negativo.
# d. Calcule a média dos dígitos de um número inteiro não negativo.
'''

def produtorio(m, n): 
    if n == 0:
        return 1
    return m * produtorio(m, n - 1)

def potencia(k, n):
    if n == 0:
        return 1
    return k * potencia(k, n - 1)

def somaDigitos(n):
    if n == 0:
        return 0
    return n % 10 + somaDigitos(n // 10) # A divisão por 10 serve para interagir apenas com o último número.

'''
Ex: somaDigitos(123)
    = 123 % 10   + somaDigitos(123 // 10)
    = 3          + somaDigitos(12)
    = 3 + 2      + somaDigitos(12 // 10)
    = 3 + 2      + somaDigitos(1)
    = 3 + 2 + 1  + somaDigitos(0 // 10)
    = 3 + 2 + 1  + somaDigitos(0)
                     return 0
    = 3 + 2 + 1
    = 6
'''

def quantidadeDigitos(n):
    if n == 0:
        return 0
    return 1 + quantidadeDigitos(n // 10)

def mediaDigitos(n):
    soma = somaDigitos(n)
    quantidade = quantidadeDigitos(n)
    if quantidade == 0: 
        return 0
    else: 
        return soma / quantidade 

def main():
    print('\nO programa irá realizar várias operações: Produtório, Potência, Soma dos Dígitos e Média dos Dígitos.')
    print('---')

    print('\n---Calculo do Produtório---')  
    m = 4
    n = 3
    print(f'O produtorio de {m} por {n} é igual a: {produtorio(m, n)}\n') # Saída: 4.4.4 = 64

    print('\n---Calculo da Potência---')
    k = 3
    n = 4
    print(f'A potência de {k} elevado a {n} é igual a: {potencia(k, n)}\n') # Saída: 3.3.3.3 = 81
    
    print('\n---Calculo da Soma dos Dígitos---')
    n = 123
    print(f'A soma dos dígitos do número "{n}" é: {somaDigitos(n)}\n') # Saída: 1+2+3 = 6
    
    print('\n---Calculo da Média dos Dígitos---')
    n = 123
    print(f'A média dos dígitos do número "{n}" é: {mediaDigitos(n)}\n') # Saída: (1+2+3)/3 = 2
    
    print('Fim do programa!')

main()
