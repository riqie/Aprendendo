'''
Faça um programa que apresente na tela um menu com as seguintes opções: 1 –
converter um ângulo em graus para radiano; 2 - calcular o seno de um ângulo, 3 –
calcular o valor de . 4 - resolver uma equação do segundo grau; 0 - sair. Depois de 
feita a opção, o programa deve chamar uma função que leia do usuário os parâmetros 
necessários para o cálculo escolhido e a seguir usar uma das funções que você já 
implementou.
'''

def menu():
    while True:
        opcao = int(input("Escolha uma opção. \n [1] Converter de graus para radianos\n [2] Calcular seno\n [3] Calcular o valor de π B\n [4] Resolver um equação de 2º grau\n [0] Sair\n :"))
        while opcao not in '12340':
            print('Opção inválida, tente novamente.')
            opcao = int(input("Escolha uma opção. \n [1] Converter de graus para radianos\n [2] Calcular seno\n [3] Calcular o valor de π B\n [4] Resolver um equação de 2º grau\n [5] Sair\n :"))
        if opcao == 1:
            return rad()
        elif opcao == 2:
            return seno()
        elif opcao == 3:
            return pi()
        elif opcao == 4:
            return 
        else:
            break
    
def rad(x):
    a = x / 180 * 3.14

    return a

def seno(x):
    y = rad(x)
    soma = 0
    grau = 1
    coef = 1
    def fatorial(a):
        valor = 1
        for i in range(a,1,-1):
            valor *= i
        return valor
    for i in range(10):
        termo = coef * (y**grau / fatorial(grau)) 
        soma += termo
        coef *= -1

    return soma

def pi(): #Usando a série de Leibniz
    qnt = (int(input("Quantas casas devemos aproximar para pi: ")))
    soma = 0
    coef = 1
    deno = 1
    for i in range(qnt):
        termo = coef * (1 / deno)
        soma += termo
        coef *= -1
        deno += 2
    pi = 4 * soma
    return pi

def equacao():
    print('Informe os termos da equação, do maior grau pro menor. \n Ax² + Bx + C = 0')
    a = (int(input("Primeiro termo: ")))
    b = (int(input("Segundo termo: ")))
    c = (int(input("Terceiro termo: ")))
    delta = b**2 - 4*a*c
    x1 = -b + (delta**(1/2)) / 2*a
    x2 = -b - (delta**(1/2)) / 2*a
    return f'As respostas que satisfazem a equação são: {x1}, {x2}'

print(pi())
print()
