'''
Exercício 7
Fazer um programa que calcule e imprima a soma de duas matrizes (a ordem das 
duas matrizes deve ser lida da entrada padrão)
'''
while True:
    l = int(input('Número de linhas:'))
    c = int(input('Número de colunas:'))
    if l > 0 and c > 0:
        break
    else:
        print('Informe valores maiores que zero!')

Ma = []
Mb = []
Mc = []

print('-'*40)
print('Informe os elementos da Matriz A')
print('-'*40)
for i in range(0, l):
    linha_a = []
    for j in range(0, c):
        n_a = int(input(f'Elemento [{i}][{j}]:'))
        linha_a.append(n_a)
    Ma.append(linha_a)

print('-'*40)
print('Informe os elementos da Matriz B')
print('-'*40)
for i in range(0, l):
    linha_b = []
    for j in range(0, c):
        n_b = int(input(f'Elemento [{i}][{j}]:'))
        linha_b.append(n_b)
    Mb.append(linha_b)

for i in range(0, l):
    linha_c = []
    for j in range(0, c):
        n_c = Ma[i][j] + Mb[i][j]
        linha_c.append(n_c)
    Mc.append(linha_c)

print('\nMa + Mb = Mc')
print(f'{Ma} + {Mb} = {Mc}')
