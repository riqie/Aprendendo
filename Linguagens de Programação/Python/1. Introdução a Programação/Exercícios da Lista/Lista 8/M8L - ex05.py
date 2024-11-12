'''
5. Implemente um programa com uma função que, dada uma lista, retorne outra lista, 
com os elementos da lista original, sem repetições.
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

def pedir_lista():
    
    n = 0 # n = número de elementos da lista 
    while n < 1:
        n = validar_entrada(f"Informe o número de elementos da lista: ")
        print()
        if n < 1:
            print(50*"=")
            print("ERRO! Informe um número inteiro maior que zero!")
            print(50*"=")

    lista_inicial = []
    for i in range(n):
        elemento = validar_entrada(f"Informe o {i+1}° elemento: ")
        lista_inicial.append(elemento)
    
    return lista_inicial

def sem_rep(valores):
    lista_final = []

    for num in valores:
        if num not in lista_final:
            lista_final.append(num)

    return lista_final

def main():
    print(f"\t{20*"-"}")
    print("\tLista sem repetições")
    print(f"\t{20*"-"}\n")

    lista_c_rep = pedir_lista()
    lista_s_rep = sem_rep(lista_c_rep)
    print(f"\nA lista sem elementos repetidos é: {lista_s_rep}")

main()