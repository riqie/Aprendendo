'''
8. Escreva uma função que dada uma matriz quadrada, verifique se ela é uma matriz 
triangular inferior.

OBS: Matriz triangular inferior = Ser Quadrada + Todos os elementos acima da diagonal principal devem ser iguais a zero
'''

def validar_entrada(msg):
    
    while True:
        try:
            valor_str = input(msg)
            valor_int = int(valor_str)
            return valor_int
        except ValueError:
            print(43*"=")
            print("ERRO! Informe um inteiro válido.")
            print(43*"=")

def criar_matriz():
    print("\tMatriz Triangular Superior")
    print(f"\t{26*"-"}\n")
    n = 1
    while n <= 2:
        n = validar_entrada("Ordem da matriz(mínimo = 2): ")
        print()
        if n >= 2:
            break
        else:
            print("Valor inválido!")
            print(35*"-")

    matriz = []
    for i in range(n):
        linha = []
        for j in range(n):
            num = validar_entrada(f"Informe o elemento [{i}][{j}]: ")
            linha.append(num)
        matriz.append(linha)

    return matriz

def analise_matriz(matriz):

    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i < j and matriz[i][j] != 0:
                return "A matriz não é uma matriz triangular inferior"

    return "A matriz é uma matriz triangular inferior"

def main():

    matriz = criar_matriz()

    resultado = analise_matriz(matriz)

    print(f"\n{resultado}\n")

main()
