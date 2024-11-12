'''
11. Uma matriz de permutações é uma matriz quadrada cujos elementos são zeros ou 
uns, tal que em cada linha e em cada coluna exista exatamente um elemento igual a 1.
Escreva um programa que, dada uma matriz quadrada, verifique se ela é uma matriz 
de permutações
'''

def validar_entrada(msg):
    
    while True:
        try:
            valor_str = input(msg)
            valor_int = int(valor_str)
            return valor_int
        except ValueError:
            print(32*"=")
            print("ERRO! Informe um inteiro válido.")
            print(32*"=")

def criar_matriz():
    print("\tMatriz de Permutações")
    print(f"\t{21*"-"}\n")
    n = 0
    while n <= 0:
        n = validar_entrada("Ordem da matriz(mínimo = 1): ")
        print()
        if n > 0:
            break
        else:
            print("Valor inválido!")
            print(35*"-")

    matriz = []
    for i in range(n):
        linha = []
        for j in range(n):
            k = -1
            while k != 0 or k != 1:
                k = validar_entrada(f"Informe o elemento [{i}][{j}]: ")
                if k == 0 or k == 1:
                    linha.append(k)
                    break
                else:
                    print(30*"=")
                    print("Valor inválido. Informe 0 ou 1")
                    print(30*"=")
        matriz.append(linha)

    return matriz


def analise_matriz(matrix):

    lista_i = []
    lista_j = []

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 1:
                if i not in lista_i and j not in lista_j:
                    lista_i.append(i)
                    lista_j.append(j)
                else:
                    return "\nA matriz não é uma matriz de permutações\n"

    return "\nA matriz é uma matriz de permutações\n"


def main():
    matriz = criar_matriz()

    resultado = analise_matriz(matriz)

    print(resultado)


main()
