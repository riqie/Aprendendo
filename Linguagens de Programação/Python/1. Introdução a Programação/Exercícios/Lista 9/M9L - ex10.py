'''
Uma matriz quadrada de números inteiros é um quadrado mágico se o valor da soma 
dos elementos de cada linha, de cada coluna e da diagonal principal e da diagonal 
secundária é o mesmo. Além disso, a matriz deve conter todos os números inteiros 
do intervalo [1..n × n]. Escreva um programa que, dada uma matriz quadrada, 
verifique se ela é um quadrado mágico
'''

def verificar_quadrado_magico(matriz):
    n = len(matriz)
    
    for linha in matriz: #verificando se é uma matriz quadrada
        if len(linha) != n:
            return False
    
    soma = sum(matriz[0]) #verificando se a soma das linhas são iguais
    for linha in matriz:
        if sum(linha) != soma:
            return False
    
    for i in range(n): #verificando se a soma das colunas são iguais
        soma_coluna = sum(matriz[linha][i] for linha in range(n))
        if soma_coluna != soma:
            return False
    
    soma_diagonal_principal = sum(matriz[i][i] for i in range(n)) #verifica a diagonal principal
    if soma_diagonal_principal != soma:
        return False
    
    soma_diagonal_secundaria = sum(matriz[i][n - 1 - i] for i in range(n)) # Verifica a diagonal secundária
    if soma_diagonal_secundaria != soma:
        return False
    
    elementos = set() # Verifica se a matriz contém todos os números do intervalo (1, n x n)
    for linha in matriz:
        for num in linha:
            elementos.add(num)
    
    if elementos != set(range(1, n*n + 1)):
        return False
    
    return True

def validar_entrada(msg):
    
    while True:
        try:
            valor_str = input(msg)
            valor_int = int(valor_str)
            return valor_int
        except ValueError:
            print(30*"=")
            print("ERRO! Digite um número inteiro")
            print(30*"=")


def criar_matriz():
    linhas = validar_entrada("Linhas: ")
    colunas = validar_entrada("Colunas: ")
    matriz = []
    for i in range(linhas):
        linha = []
        for i in range(colunas):
            valor = validar_entrada("Adicione um valor: ")
            linha.append(valor)
        matriz.append(linha)
    return matriz

def main():
    print("Quadrados mágicos")
    print("-"*80)
    matriz = criar_matriz()
    verificar = verificar_quadrado_magico(matriz)
    if verificar == True:
        return "É um quadrado perfeito."
    else:
        return "Não é um quadrado perfeito."
    
print(main())

'''
exemplo de quadrado perfeito
4 3 8
9 5 1
2 7 6
'''
