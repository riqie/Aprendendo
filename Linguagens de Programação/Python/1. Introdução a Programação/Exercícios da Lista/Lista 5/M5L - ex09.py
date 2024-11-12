'''
Fazer um programa que calcule e imprima o produto por um escalar de uma matriz
qualquer com dimensões máximas de 20x20
'''

linhas = -1
colunas = -1


while linhas <= 0 or colunas <= 0:
    linhas = int(input("Entre com a quantidade de linhas (tam. máx= 20): "))
    colunas = int(input("Entre com a quantidade de colunas (tam. máx= 20): "))
    print("-"*40)

    if linhas > 20 or colunas > 20:
        print ("O tamanho é maior que 20.")
        print ("Tente novamente!")
        break


matriz = [[0 for _ in range(colunas)] for _ in range(linhas)]

for i in range (linhas):
    for j in range (colunas):
        valor = float(input(f"Digite o valor para a posição ({i + 1}, {j + 1}): "))
        matriz[i][j] = valor
print("-"*40)

print("Matriz:")
for linha in matriz:
    print(linha)
print("-"*40)
escalar = int(input("Entre com o escalar: "))

for i in range(linhas):
    for j in range (colunas):
        matriz[i][j] *= escalarsss

print("Matriz após a multiplicação pelo escalar:")
for linha in matriz:
    print(linha)
print("-"*40)
