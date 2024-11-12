'''
Faça um programa que apresente na tela um menu com as seguintes opções: 1 –
converter um ângulo em graus para radiano; 2 - calcular o seno de um ângulo, 3 –
calcular o valor de . 4 - resolver uma equação do segundo grau; 0 - sair. Depois de
feita a opção, o programa deve chamar uma função que leia do usuário os parâmetros
necessários para o cálculo escolhido e a seguir usar uma das funções que você já
implementou.
'''

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

def menu():
    while True:
        opcao = validar_entrada("Escolha uma opção. \n [1] Converter de graus para radianos\n [2] Calcular seno\n [3] Calcular o valor de π \n [4] Resolver um equação de 2º grau\n [0] Sair\n :")
        while opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 0:
            print('Opção inválida, tente novamente.')
            opcao = validar_entrada("Escolha uma opção. \n [1] Converter de graus para radianos\n [2] Calcular seno\n [3] Calcular o valor de π \n [4] Resolver um equação de 2º grau\n [0] Sair\n :")
        if opcao == 1:
            return 1
        elif opcao == 2:
            return 2
        elif opcao == 3:
            return 3
        elif opcao == 4:
            return 4
        else:
            break
    
def rad():
    x = validar_entrada("Valor para transformar em radiano: ") 
    a = x / 180
    return f"{a:.4f}π"

def seno():
    x = validar_entrada("Valor para buscar o seno: ")
    qnt = validar_entrada("Quantas casas devemos aproximar o seno: ")
    y = x / 180 * 3.14
    soma = 0
    grau = 1
    coef = 1
    def fatorial(a):
        valor = 1
        for i in range(a,1,-1):
            valor *= i
        return valor
    for i in range(qnt):
        termo = coef * (y**grau / fatorial(grau)) 
        soma += termo
        coef *= -1

    return soma

def pi(): #Usando a série de Leibniz
    print("Calculando pi...")
    soma = 0
    coef = 1
    deno = 1
    for i in range(50):
        termo = coef * (1 / deno)
        soma += termo
        coef *= -1
        deno += 2
    pi = 4 * soma
    return pi

def equacao():
    print('Informe os termos da equação, do maior grau pro menor. \n Ax² + Bx + C = 0')
    a = validar_entrada("Primeiro termo: ")
    b = validar_entrada("Segundo termo: ")
    c = validar_entrada("Terceiro termo: ")
    delta = b**2 - 4*a*c
    x1 = -b + (delta**(1/2)) / 2*a
    x2 = -b - (delta**(1/2)) / 2*a
    return f'As respostas que satisfazem a equação são: {x1}, {x2}'

def main():
    print("Calculadora matemática")
    print("-"*80)
    opcao = menu()
    if opcao == 1:
        resposta = rad()
        return resposta
    elif opcao == 2:
        resposta = seno()
        return resposta
    elif opcao == 3:
        resposta = pi()
        return resposta
    elif opcao == 4:
        resposta = equacao()
        return resposta
    else:
        return 'Fim do programa.'
    
print(main())
