# 15. Elabore um programa que calcule e mostre a soma dos 10 primeiros termos da s�rie:
# 100/0! + 99/1! + 98/2! + ...

def fatorial(i):
    resultado = 1
    
    for j in range(2, i + 1):
        resultado *= j
    return resultado

def calcular_soma_serie(numeroTermos):
    soma = 0

    for i in range(numeroTermos):
        termo = (100 - i) / fatorial(i)
        soma += termo
    return soma

def main():
    print('\nO programa a seguir realizará a soma dos 10 primeiros termos da sequência antes mencionada.\n')
    
    numeroTermos = 13
    soma_serie = calcular_soma_serie(numeroTermos)

    print(f"A soma dos {numeroTermos} primeiros termos da série é: {soma_serie:.5f}")
    print('\nfim do programa.')

main()
# o código só faz até os 10 prieiros termos, arrumar isso para quantos termos quiser.
