def main():
    linhas = int(input('Entre o numero de lines: '))
    colunas = int(input('entre o numero de clumns: '))
    matriz = []

    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(colunas)
        matriz.append(linha)
        
    print(matriz)

main()

