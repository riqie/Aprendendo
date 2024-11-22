'''
Defina uma função recursiva que recebe como argumento uma lista de listas de 
números inteiros w e devolve o número de listas em w ordenadas por ordem 
crescente em sentido lato, ou seja, em que cada elemento é menor ou igual que o 
seguinte. Por exemplo, no caso da lista [[2,2,3,0],[1,2,5,4],[2,4,4]] a função deve 
devolver 1 pois só a terceira lista está ordenada
'''

def verificar(matriz):
    print(matriz)
    print(matriz[1:])
    if matriz == []: #Verifica se a matriz é vazia
        return 0
    
    if matriz[0] == sorted(matriz[0]):
        
        return 1 + verificar(matriz[1:])

    return verificar(matriz[1:])

def main():

    print("\tLISTAS ORDENADAS DE FORMA CRESCENTE EM SENTIDO LATO\n")

    resultado = verificar([[1,2,5,4],[1,2,5,2],[2,4,1],[2,2,4]])

    print(f"A lista w possui {resultado} listas ordenadas")
    print()

main()


