# Escreva uma função que dada uma matriz (M), calcule a sua transposta (Mt)


def criarMatriz():

    print('='*60)
    print('O programa vai criar uma matriz de acordo com o input do usuário e depois fará a transposta a partir da primeira.')

    while True:

        print('='*60)
        linhas = input("Digite o número de linhas da matriz: ")
        colunas = input("Digite o número de colunas da matriz: ")

        # Verificação para não dar erro
        if not (linhas.isdigit() and colunas.isdigit()):
            print('='*60)
            print("Valor para colunas ou linhas está inválido. Tente novamente.")
            continue

        linhas = int(linhas)
        colunas = int(colunas)

        # Criando a matriz
        matriz = []

        for i in range(linhas):
            linha = []

            for j in range(colunas):

                while True:
                    valor = input(f"Digite o valor para a posição ({i+1}, {j+1}): ")

                    try:
                        valor = float(valor)  # Permite números decimais
                        linha.append(valor)
                        break
                    
                    except ValueError:
                        print('='*60)
                        print("Por favor, digite um número válido.")

            matriz.append(linha)

        print('Esta é a matriz Original: ')

        # Imprimindo a matriz original
        for linha in matriz:
            for valor in linha:
                print(f"{valor:.2f}", end=' ')

            print()

        return matriz



def transposta(matriz):

    linhas = len(matriz)
    colunas = len(matriz[0])
    
    matriz_transposta = []

    for j in range(colunas):
        nova_linha = []

        for i in range(linhas):
            nova_linha.append(matriz[i][j])

        matriz_transposta.append(nova_linha)
    
    print("Esta é a matriz Transposta: ")

    # Imprimindo a matriz transposta
    for linha in matriz_transposta:
        for valor in linha:
            print(f"{valor:.2f}", end=' ')

        print()

    return matriz_transposta



def main():
    matriz = criarMatriz()
    transposta(matriz)

main()
