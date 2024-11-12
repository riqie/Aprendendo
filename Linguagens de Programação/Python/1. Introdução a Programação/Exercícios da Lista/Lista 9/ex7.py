'''
Escreva uma função que dada uma matriz quadrada, verifique se ela é uma matriz 
diagonal
'''

def conj(lista1, lista2):
    primeiro = set(lista1)
    segundo = set(lista2)

    uniao = primeiro | segundo
    intersec = primeiro & segundo
    dif1 = primeiro - segundo
    dif2 = segundo - primeiro
    contem = primeiro.issubset(segundo)

    return f'união = {uniao}, intersecção {intersec}, \n temos 2 possibilidades de diferenças: {dif1} e {dif2} \n e por fim a pergunta se a primeira lista está contida na segunda: {contem}'
        
lista = [1,2,3,4,5]
lista2 = [2,3,4,5,6,7]
print(conj(lista, lista2))
