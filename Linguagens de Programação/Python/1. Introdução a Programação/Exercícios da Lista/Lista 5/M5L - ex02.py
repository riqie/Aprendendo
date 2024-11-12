'''
Exercício 2
Dadas duas listas L1 e L2, com n e m valores inteiros, respectivamente,escreva um programa que concatene as listas L1 e L2 em uma nova lista L3. Em seguida, imprima a lista L3 ordenada de maneira crescente e decrescente.
'''
while True:
    print(50*"-")
    n = int(input('Quantos valores inteiros terá a lista L1? '))
    m = int(input('Quantos valores inteiros terá a lista L2? '))
    print(50*"-")

    if n > 0 and m > 0:
        break
    else:
        print('Informe valores maiores que zero!')

l1 = []
l2 = []

for c in range(n):
    l1.append(int(input('Informe um número inteiro para L1: ')))

print(50*"-")

for c in range(m):
    l1.append(int(input('Informe um número inteiro para L2: ')))

print(50*"-")

l3 = l1 + l2

l3.sort()
print(f'Lista L3 ordenada de maneira crescente: {l3}')

l3.sort(reverse = True)
print(f'Lista L3 ordenada de maneira decrescente: {l3}')

print(50*"-")
