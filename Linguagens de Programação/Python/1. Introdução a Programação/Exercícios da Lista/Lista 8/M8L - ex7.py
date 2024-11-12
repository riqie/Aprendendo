'''
Crie um programa que implemente e teste uma função que, dadas duas listas
representando dois conjuntos:
a. Retorne uma lista que represente a união dos dois conjuntos.
b. Retorne uma lista que represente a interseção dos dois conjuntos.
c. Retorne uma lista que represente a diferença entre os dois conjuntos.
d. Verifique se o primeiro é um subconjunto do segundo.
'''
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

def preencher():
    lista  = []
    qnt = validar_entrada("Quantidade de itens na lista: ")
    for i in range(qnt):
        valor = input("Valor: ")
        lista.append(valor)
    return lista

def menu(x,y):
    opcao = validar_entrada("Escolha uma opção. \n [1] União dos conjuntos\n [2] Intersecção dos conjuntos\n [3] Diferença entre conjuntos\n [4] Os conjuntos são subconjuntos?\n :")
    while opcao != 1 and opcao !=2 and opcao != 3 and opcao != 4 and opcao != 5:
        print('Opção inválida, tente novamente.')
        opcao = int(input("Escolha uma opção. \n [1] União dos conjuntos\n [2] Intersecção dos conjuntos\n [3] Diferença entre conjuntos\n [4] Os conjuntos são subconjuntos?\n :"))
    if opcao == 1:
        return uniao(x,y)
    elif opcao == 2:
        return intersec(x,y)
    elif opcao == 3:
        return diferenca(x,y)
    else:
        return subconj(x,y)

def uniao(x, y):
    resultado = x | y
    return list(resultado)

def intersec(x,y):
    resultado = x & y
    return list(resultado)

def diferenca(x,y):
    primeiro = x - y
    segundo = y - x
    return primeiro, segundo

def subconj(x,y):
    contem = x.issubset(y)
    contem2 = y.issubset(x)
    return f"O primeiro é subconjunto do segundo: {contem} \n O segundo é subconjunto do primeiro: {contem2}"
        
def main():
    print("Operações com conjuntos")
    print("-"*80)
    lista1 = preencher()
    lista2 = preencher()
    lista1 = set(lista1)
    lista2 = set(lista2)

    resultado = menu(lista1,lista2)
    return resultado

print(main())
