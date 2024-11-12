'''
7. Escreva uma função que dada uma matriz quadrada, verifique se ela é uma matriz 
diagonal.

OBS: Matriz diagonal = Ser Quadrada + Todos os elementos fora da diagonal principal iguais a zero
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

    n = 0
    while n < 1:
        n = validar_entrada("Ordem da matriz(mínimo = 1): ")
        if n >= 1:
            print()
            break
        else:
            print(43*"=")
            print("ERRO! Informe um inteiro maior ou igual a 1")
            print(43*"=")

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
            if i != j and matriz[i][j] != 0:
                return "A matriz não é uma matriz diagonal"
    
    return "A matriz é uma matriz diagonal"

def main():
    print(f"\t{15*"-"}")
    print("\tMatriz Diagonal")
    print(f"\t{15*"-"}\n")

    matriz = criar_matriz()

    resultado = analise_matriz(matriz)

    print(f"\n{resultado}\n")

main()