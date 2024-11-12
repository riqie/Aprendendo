'''
6. Crie um programa que implemente uma função que, dada uma lista, retorne a moda 
da lista, ou seja, uma lista com o(s) elemento(s) mais frequente(s) da lista original.
'''

def validar_entrada(msg):
    
    while True:
        try:
            valor_str = input(msg)
            valor_int = int(valor_str)
            return valor_int
        except ValueError:
            print(47*"=")
            print("ERRO! Informe um número inteiro maior que zero!")
            print(47*"=")

def pedir_lista():
    n = 0
    lista = []

    while n < 1:
        n = validar_entrada("Informe o número de elementos da lista: ")

        if n < 1:
            print(47*"=")
            print("ERRO! Informe um número inteiro maior que zero!")
            print(47*"=")

    cont = 0  
    while cont < n:
        num = validar_entrada(f"Informe o {cont+1}° número: ")
        lista.append(num)
        cont += 1

    return lista

def moda(valores):
    frequencias = {}
    #Criando dicionario que armazenará a frequência de cada número da lista
    for num in valores:
        frequencias[num] = frequencias.get(num, 0) + 1

    if max(frequencias.values()) == 1:
        return []
    else:
        return [chave for chave in frequencias.keys() if frequencias[chave] == max(frequencias.values())]

def main():
    print(f"\t{17*"-"}")
    print("\tModa de uma lista")
    print(f"\t{17*"-"}\n")

    lista = pedir_lista()

    moda_lista = moda(lista)
    
    print(f"\nA moda da lista é {moda_lista}")

main() 

