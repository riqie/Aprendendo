'''
Escreva uma função que, dados dois números inteiros positivos, calcule e retorne o
Máximo Divisor Comum (MDC) entre os dois. Escreva também uma função que, dada
uma lista de três ou mais números inteiros positivos, calcule e retorne o Máximo
Divisor Comum (MDC) entre eles. A seguir, escreva um programa para testar essas
funções.
'''


def duplo(x,y):
    if x < 0: #modularizando os valores caso sejam negativos
        x = 0 - x
    if y < 0:
        y = 0 - y

    if x == 0 or y == 0: #caso algum for 0
        return max(x,y)
    
    if x == y:
        return x
    
    valor = max(x,y)
    for i in range(1, valor):
        if x % i == 0 and y % i == 0:
            fator = i
    return fator

def listar():
    lst = []
    qnt = validar_entrada("Quantidade de elementos: ")
    while qnt <= 0:
        print("ERRO! Insira um valor maior do que 0.")
        qnt = validar_entrada("Quantidade de elementos: ")
    for i in range(qnt):
        valor = validar_entrada("Insira um valor: ")
        lst.append(valor)
    fator = lst[0]
    for i in lst[1:]:
        fator = duplo(fator, i)
    return fator

def validar_entrada(msg):
    
    while True:
        try:
            valor_str = input(msg)
            valor_int = int(valor_str)
            return valor_int
        except ValueError:
            print(30*"=")
            print("ERRO! Digite um número inteiro")
            print(30*"=")

def escolha():

    print("Qual operação deseja relizar")
    esc = validar_entrada("[1] MDC entre 2 números \n[2] MDC dos valores de uma lista com 3 ou mais elementos\n :")
    while esc != 1 and esc != 2:
        print("Valor inválido. Tente novamente.")
        esc = validar_entrada("[1] MDC entre 2 números \n[2] MDC dos valores de uma lista com 3 ou mais elementos\n :")
    return esc

def main():
    print("Calculos de MDC")
    print("-"*80)
    esc = escolha()
    if esc == 1:
        x = validar_entrada("Informe o primeiro número: ")
        y = validar_entrada("Informe o segundo elemento: ")
        resultado = duplo(x,y)
        return f'O resultado é: {resultado}'
    else:
        resultado = listar()
        return f'O resultado é: {resultado}'

print(main())
