'''
Defina uma função recursiva que recebe como argumento uma lista de listas de
números inteiros w e devolve True se em todas as sublistas de w existir um número
positivo. Por exemplo, no caso da lista [[2,4,3,1],[3,-5,-7],[],[8,0,-6]] a função deve
devolver False porque em [] não existe nenhum número positivo.
'''

def positivos(lista):
    if lista == []:  # Caso lista vazia
        return False
    primeira = lista[0]  # Pega a primeira sublista
    if primeira == []: # Caso primeira lista vazia
        return False
    if len(lista) == 1:
        for x in primeira:
            if x > 0:
                return True
        return False
    for x in primeira:  # Começa a iterar a primeira sublista
        if x > 0:
            return positivos(lista[1:]) #Caso encontre um número positivo já começa a iterar a próxima sublista
    return False #Caso não encontre nenhum positivo já vai retornar falso

def main():
    print("Verificando se existem números positivos em listas de listas")
    lista = [[-1,2,3],[2,3,4],[6,7,8],[2]]
    return positivos(lista)

print(main())
