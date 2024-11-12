# 3. Escreva uma função que imprime, linha a linha, os valores de uma matriz 
# bidimensional dada como argumento.

# Função para exibir a matriz
def imprimir_matriz(matriz):
    print('='*60)
    
    for linha in matriz:
        for valor in linha:
            print(valor, end=' ')
        print()

# Função para receber os valores que serão enviados como parâmetro para criar a matriz
def obter_matriz_do_usuario():
    print('='*60)
    print('O programa vai criar uma matriz de acordo com o input do usuário.')
    while True:
        print('='*60)
        linhas = input("Digite o número de linhas da matriz: ")
        colunas = input("Digite o número de colunas da matriz: ")

        # Verificação para não dar erro
        if not (linhas.isdigit() and colunas.isdigit()):
            print('='*60)
            print("Valor para colunas ou linhas está inválido. Tente novamente.")
            continue

        else:
            linhas = int(linhas)
            colunas = int(colunas)

        # Criando a matriz
        matriz = []
        for i in range(linhas):
            linha = []

            for j in range(colunas):
                while True:
                    valor = input(f"Digite o valor para a posição ({i+1}, {j+1}): ")

                    if valor.isdigit():
                        linha.append(int(valor))
                        break

                    else:
                        print('='*60)
                        print("Por favor, digite um número inteiro.")

            matriz.append(linha)
        
        return matriz

def main():
    matriz_usuario = obter_matriz_do_usuario()
    imprimir_matriz(matriz_usuario)

main()
print('fim do programa.')
