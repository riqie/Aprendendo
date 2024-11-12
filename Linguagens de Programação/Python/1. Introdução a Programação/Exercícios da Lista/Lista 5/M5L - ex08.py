'''
Faça um programa que leia as dimensões de uma matriz qualquer (no máximo 30x30),
leia seus elementos e imprima a sua transposta.
'''

print("Programa para foramr matrizes e transcreve-lás para matrizes transpostas")
print("-"*80)
print("Quais serão as dimensões da matriz? (max 30x30)")

#informando o tamanho da matriz
linhas = int(input("Número de linhas? "))
if linhas > 30 or linhas <= 0:
    print("número inválido, tente novamente.")
    linhas = int(input("Número de linhas? "))

colunas = int(input("Número de colunas? "))
if colunas > 30 or colunas <= 0:
    print("número inválido, tente novamente.")
    colunas = int(input("Número de colunas? "))

#adicionando elementos a matriz com o tamanho escolhido
print(f"A sua matriz tem o tamanho de {linhas}x{colunas}")
print("Vamos adicionar os elementos")
print("Começando pela primeira linha, da esquerda para a direita")
print("Depois vamos para a seguinda linha e assim por diante")

matriz = []
linha = []
colunas2 = colunas
linhas2 = linhas
linhas3 = linhas

while linhas > 0:
    while colunas > 0:
        elemento = str(input("Adicionar: "))
        linha.append(elemento)
        colunas = colunas - 1
    print("Próxima linha.")
    matriz.append(linha)
    linha = []
    linhas = linhas - 1
    colunas = colunas2

print("Sua matriz está assim.")
for a in matriz:
    print(a)

print("Agora vamos escreve-lá da forma transposta")

matriz_transposta = list(zip(*matriz))

for a in matriz_transposta:
    print(a)
