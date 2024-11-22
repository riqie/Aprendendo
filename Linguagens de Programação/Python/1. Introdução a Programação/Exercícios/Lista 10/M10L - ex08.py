'''
Defina a função que recebe como argumento um número inteiro positivo e devolve 
True se esse número for um número perfeito e False em caso contrário. Recorde que 
um número perfeito é um número natural que é igual à soma de todos os seus 
divisores próprios, isto é, a soma de todos os divisores excluindo o próprio número. 
Pode, se assim o entender, definir funções auxiliares.

Ex: 6 é um número perfeito? (1 + 2 + 3 = 6 -> Logo, 6 é um número perfeito)
Ex: 18 é um número perfeito? (1 + 2 + 3 + 6 + 9 = 21 -> Logo, 18 não é um número perfeito)
'''

def divisores(n, i = 1):
    if (i >= (n // 2) + 1): 
        return []

    if (n % i == 0):
        return [i] + divisores(n, i + 1)
    
    return divisores(n, i + 1)

def numero_perfeito(n):

    todos_divisores = divisores(n)
    num_perfeito = sum(todos_divisores)

    return num_perfeito == n

def main():

    print("\tNÚMERO PERFEITO\n")

    num = 18 
    resultado = numero_perfeito(num)

    print(f"O número {num} é perfeito? {resultado}")

main()

