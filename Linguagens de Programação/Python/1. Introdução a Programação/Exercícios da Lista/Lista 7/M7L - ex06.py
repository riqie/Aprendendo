'''
Faça um programa que encontre todas as chaves que estão associadas a um
determinado valor em um dicionário. O programa deve preencher um dicionário pelo
usuário e, a partir desse dicionário e de um valor indicado pelo usuário, encontrar e
exibir as chaves relacionadas ao valor em forma de lista.
'''

valores = {}
total = []

qnt = int(input('Quantos itens chave-valor deseja adicionar? '))
for i in range(qnt):
    chave = input('Começando pela chave: ')
    valor = input('Agora, insira um valor: ')
    valores[chave] = valor

print('Agora, vamos consultar valores de acordo com a chave.')
busca = input('Qual valor devemos buscar? ')
for chave, valor in valores.items():
    if valor == busca:
        total.append(chave)
    
if len(total) == 0:
    print('Esse valor não existe.')
    print(total)
else:
    print(f'Existem {len(total)} chaves correspondentes a esse valor.')
    print(total)
