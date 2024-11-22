'''
3. Faça um programa para calcular a média de um conjunto de 15 valores dados pelo
usuário e armazenados em um vetor. Ao final, imprima a média e todos os valores
digitados que ficaram abaixo da média.
'''
# informando o programa ao usuario
print("="*115)
print(" Este programa irá ler 15 números, fazer a média destes e no final dirá quais ficaram abaixo da média, caso haja.")
print("="*115)

# definindo as variáveis
qntd = 15
N = 1          #variavel para a interface
numeros = []
abaixo_media = []

# criando uma "interface" para o usuário
print("-"*40)
print(f" Insira os {qntd} números.")
print("-"*40)

while N <= 15:
    for i in range(qntd):
        numeros.append(int(input(f"{N}° Número: ")))
        N += 1

print("-"*40)
print(f'Números inseridos: {numeros}.')
print("-"*40)
print("Calculando a média...")

import time
for i in range(3):
    time.sleep(1)
    print("...")

# definindo últimas variáveis
soma = sum(numeros)
media = soma/len(numeros)
print(f"O resultado da média foi: {media:.2f} .")
print("-"*40)

# comoando para ler os numeros, dentro da lista, que ficaram abaixo da media e imprimir resultado
for abaixo in numeros:
    if abaixo < media:
        abaixo_media.append(abaixo)

if abaixo_media == []:
    print(" Não existem números abaixo da média.")
    print("-"*40)
else:
    print(" Os números que ficaram abaixo da média foram:", abaixo_media)
    print("-"*40)

# fim gg
print("="*40)
print(" Fim do programa.")
print("="*40)

