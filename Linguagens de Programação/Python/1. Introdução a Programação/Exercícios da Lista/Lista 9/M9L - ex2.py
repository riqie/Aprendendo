'''
Escreva uma função que, dada uma lista bidimensional (lista de listas), verifique 
se ela é uma matriz. Em caso positivo, sua função deve retornar uma tupla com o 
número de linhas e de colunas da matriz. Em caso negativo, deve retornar uma 
tupla vazia
'''

def verificar_matriz(lst):
    if lst == []: 
        return ()
    
    tamanho = len(lst[0])
    colunas = 0
    for i in lst:
        if len(i) != tamanho:
            return "Não é uma matriz."
        colunas += 1
    return (tamanho, colunas)

def main(x):
    print("Verificando matrizes.")
    resultado = verificar_matriz(x)
    return resultado

matriz = [[1,2,3],[2,1,4],[3,4,5]]

print(main(matriz))
