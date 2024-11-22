'''
# Defina uma função recursiva que recebe como argumento uma lista de listas de
# números inteiros w e devolve True se cada lista em w tiver igual número de
# elementos positivos e negativos, e False em caso contrário. Por exemplo, no caso da
# lista [[2,4,-3,-1],[-3,0,7],[-8,6]] a função deve devolver True pois todas as listas têm
# igual número de elementos positivos e negativos.
'''

def conta_positivos_negativos(lista, cont=0, positivos=0, negativos=0):
    if cont == len(lista):
        return positivos == negativos
    
    if lista[cont] > 0:
        positivos += 1
    elif lista[cont] < 0:
        negativos += 1
    
    return conta_positivos_negativos(lista, cont + 1, positivos, negativos)
'''
se 'w' for vazio ou zero, ou seja, se nao tiver elementos positivos ou negativos, tecnicamente o numero deeles são iguais (0), então retorna True.

caso contrário:

    o "if lista[cont] > 0" e o "elif lista[cont] < 0" basicamente vai checar se o número é negativo ou positivo,adicionando 1 para cada qual.

    depois ele vai chamar a função novamente, porem o contador vai somar 1, fazendo com que ele percorra o próximo elemento da lista.

    esta função apenas checa os elementos de 1 lista, a próxima função que irá checar para outras listas.
'''

def verifica_todas_listas(w):
    if not w:
        return True
    
    if not conta_positivos_negativos(w[0]):
        return False
    
    return verifica_todas_listas(w[1:])
'''
"verifica_todas_listas(w[1:])" 
fará com que a verificação dos números passe para as próximas listas.
retornando True caso a primeira função (cont_positivos_negativos) seja True ou False caso contrário.
'''

def main():
    print('\nO programa vai ler uma lista de listas "w" e verificar se cada uma tem número de elementos positivos e negativos iguais.\n\nSe forem iguais: Resultado = True, caso contrário: Resultado = False')

    w = [[2, 4, -3, -1], [-3, 0, 7], [-8, 6]]
    resultado = verifica_todas_listas(w)
    print('\nExemplo 1:\nLista "w":', w,)
    print('Resultado =', resultado)

    w = [[1, 4, 0, -1], [0, 0, 7], [-8, 6]]
    resultado = verifica_todas_listas(w)
    print('\nExemplo 2:\nLista "w":', w,)
    print('Resultado =', resultado)

    print('\nFim do programa')

main()
