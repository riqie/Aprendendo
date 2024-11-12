# Escreva uma função que recebe duas matrizes (A e B). Se as duas matrizes tiverem 
# dimensões compatíveis, sua função deve retornar a soma das duas (C = A + B). Caso 
# contrário, sua função deve retornar uma lista vazia.

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

    if A == [] and B == []:
        
        C = []
        print(f'Lista C vazia: {C}')

        return False

    return matrizes

def somarMatrizes(A, B):

    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return []
    
    C = []

    for i in range(len(A)):
        linha_c = []

        for j in range(len(A[0])):
            linha_c.append(A[i][j] + B[i][j])
        C.append(linha_c)
    
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

        print("Matriz soma (C = A + B):")
        for linha in C:
            for elemento in linha:
                print(elemento, end=' ')
            print()
    else:
        print("As matrizes têm dimensões incompatíveis e não podem ser somadas.")


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
        print('Reinicie o programa!')
        return

    validar_entrada(matrizes)
    A, B = matrizes
    C = somarMatrizes(A, B)
    exibicao(A, B, C)

main()
