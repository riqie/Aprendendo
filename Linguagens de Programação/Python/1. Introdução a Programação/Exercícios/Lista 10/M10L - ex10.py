'''
Usando algoritmos recursivos, escreva funções que:
a. Defina uma função que recebe como argumento uma lista de inteiros e devolva
o produto dos seus elementos.
b. Defina uma função que recebe como argumento uma lista de números inteiros
w e devolve True se w contém um número par e False em caso contrário.
c. Defina uma função que recebe como argumento uma lista de números inteiros
w e devolve True se w contém apenas números ímpares e False em caso
contrário
'''

def produto(lst):
    if lst == []:  #caso lista vazia
        return 0
    if len(lst) == 1: #caso para chegar ao último elemento da lista
        return lst[0]
    return lst[0] * produto(lst[1:])

def pares(lst):
    if lst == []: #caso da lista vazia
        return False
    if lst[0] % 2 == 0: #análise de cada caso
        return True
    return pares(lst[1:])

def impar(lst):
    if lst == []: #Caso a função receba uma lista vazia
        return False
    if len(lst) == 1: #Condição para evitar chegar à lista vazia 
        if lst[0] % 2 == 0: #Avaliação do ultimo termo
            return False
        return True
    if lst[0] % 2 == 1: #Análise de cada condição chamando a função novamente
        return impar(lst[1:])
    return False
        
def main():
    print("Vamos analisar uma lista")
    print("=" *80)
    lista = [1,2,3,4,5]
    print(lista)
    print("Multiplicando os valores da lista...")
    print(produto(lista))
    print("=" *80)
    print("Avaliando números pares na lista...")
    print(pares(lista))
    print("=" *80)
    print("Verificando uma lista apenas de números ímpares...")
    print(impar(lista))

print(main())
