'''
Usando algoritmos recursivos, escreva funções que:
a. Obtenha o máximo de uma lista.
b. Obtenha o máximo de uma lista com n números.
c. Buscar um caractere c em uma string s a partir de uma posição index e retornar a
posição da primeira ocorrência deste caractere (caso encontre) ou −1 (caso
contrário).
'''

def maior(lst):
    if lst == [] :
        return "Lista vazia."
    if len(lst) == 1:
        return lst[0]
    elemento = lst[0]
    maior_resto = maior(lst[1:])
    if elemento > maior_resto:
        return elemento
    else:
        return maior_resto
    
def receber_lista(n):
    lista = []
    while n > 0:
        valor = input("Insira um valor: ")
        lista.append(valor)
        n -= 1
    return maior(lista)

def posicao(str, c, index):
    if c not in str:
        return -1
    if str[index] == c:
        return index
    return posicao(str, c, index+1)

def menu():
    opcao = -1
    while opcao < 1 or opcao > 3:
        print("=" *80)
        print(
            '''            [1] Obter o maior valor de uma lista
            [2] Obter o maior valor de uma lista com n elementos
            [3] Buscar a posição index de um caractere em uma string''')
        print("=" *80)
        opcao = int(input("Digite a sua opção: "))
        if opcao < 1 or opcao > 3:
            print("Opção Inválida")
        else:
            return opcao    

def main():
    opcao = menu()
    if opcao == 1:
        print("="*80)
        print("Obtendo o máximo de uma lista")
        lista = [1,2,32,2,2]
        print(lista)
        return maior(lista)
    elif opcao == 2:
        print("="*80)
        print("Obtendo o máximo de uma lista com n elementos")
        qnt = int(input("Quantos elementos deseja inserir na lista: "))
        return receber_lista(qnt)
    else:
        print("="*80)
        print("Buscando a primeira ocorrencia e o index de um caracter na string (-1 caso não exista)")
        string = str(input("String: "))
        caracter = str(input("Caracter: "))
        return posicao(string,caracter,0)
    
print(main())
