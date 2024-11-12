# Escreva uma função que recebe duas matrizes (A e B). Se as duas matrizes tiverem 
# dimensões compatíveis, sua função deve retornar o produto das duas (C = A × B). 
# Caso contrário, sua função deve retornar uma lista vazia

def preencherMatrizes():
    A = []
    B = []
    matrizes = [A, B]

    for elementos_matriz in range(len(matrizes)):

        matriz = matrizes[elementos_matriz]

        linhas = validar_entrada(f"Digite o número de linhas da {elementos_matriz + 1}° matriz: ")
        colunas = validar_entrada(f"Digite o número de colunas da {elementos_matriz + 1}° matriz: ")

        # Preenchendo a matriz
        for i in range(linhas):
            linha_matriz = []

            for j in range(colunas):
                valor = validar_entrada(f"Digite o valor para a posição ({i+1}, {j+1}): ")
                linha_matriz.append(valor)
                
            matriz.append(linha_matriz)
    
    if A == [] or B == []:
        return False

    return matrizes

def multiplicarMatrizes(A, B):
    # Verifica se as dimensões são compatíveis para multiplicação
    if len(A[0]) != len(B):
        return []

    # Inicializa a matriz resultado C com zeros
    numero_linhas_A = len(A)
    numero_colunas_B = len(B[0])
    numero_colunas_A = len(A[0])

    C = []

    for i in range(numero_linhas_A):
        linha_C = []

        for j in range(numero_colunas_B):
            soma = 0

            for k in range(numero_colunas_A):
                soma += A[i][k] * B[k][j]

            linha_C.append(soma)

        C.append(linha_C)

    return C


def exibicao(A, B, C):

    for elementos_matriz in range(len([A, B])):
        matriz = [A, B][elementos_matriz]

        print(f"Matriz {elementos_matriz + 1}:")

        for linha in matriz:
            for elemento in linha:
                print(elemento, end=' ')
            print()

        print()

    if C:

        print("Matriz produto (C = A × B):")

        for linha in C:
            for elemento in linha:
                print(elemento, end=' ')

            print()
    else:
        print("As matrizes têm dimensões incompatíveis e não podem ser multiplicadas.")

def validar_entrada(entrada):

    while True:
        try:
            valor = int(input(entrada))

            if valor < 0:
                print("Por favor, insira um número inteiro não-negativo.")

            else:
                return valor
            
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")

def main():

    matrizes = preencherMatrizes()

    if matrizes == False:
        print("Os valores das duas matrizes prcisam ser acima de 0!")
        return
    
    A, B = matrizes
    C = multiplicarMatrizes(A, B)
    exibicao(A, B, C)

main()
