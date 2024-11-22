'''
10. A multiplicação entre dois números inteiros pode ser definida como uma repetição da 
adição de um deles. Exemplo: 3x4 = 4 + 4 + 4. Escreva uma função que multiplique 
dois números inteiros utilizando esse método. A seguir, escreva um programa que 
peça ao usuário um número inteiro e imprima a tabuada para aquele número (de 1 à 
10) utilizando a função construída.
'''

def multiplicacao(m, n):
    
    soma = 0

    print(f"\n{m:2} x {n} = ",end = '')

    for c in range(1,m+1):
        soma += n
        if c != m:
            print(n, end= ' + ')
        else:
            print(n, "=", soma)
    
def tabuada():
    while True:
        try:
            t = int(input("Tabuada do número = "))
            for i in range(1,10+1):
                multiplicacao(m=i, n=t)
        except ValueError:
            print(37*"-")
            print("Informe um número inteiro maior que 0")
            print(37*"-")

def main():

    tabuada()

main()