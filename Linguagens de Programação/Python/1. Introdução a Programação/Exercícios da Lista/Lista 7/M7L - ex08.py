'''
Exercício 8.
Escreva um programa que receba um dicionário d e retorna um dicionário “inverso” 
do dicionário dado, onde, a cada valor v de d está associada a lista das chaves de d 
que levam a v. 
Exemplos:
    >> inva( {1:2, 3:1, 4:2} )
    {2: [1, 4], 1: [3]}
    >> inva( {} )
    {}
    >> inva( {2:1, 1:2} )
    {1: [2], 2: [1]} 
'''

d = {}
inv = {}

n = int(input("Número de elementos(chave+valor) do dicionário: "))

for c in range(n):
    print(15*'-')
    chave = (input(f"{c+1}° Chave = "))
    valor = (input(f"{c+1}° Valor = "))
    d[chave] = valor

for chave, valor in d.items():
    if valor not in inv:
        inv[valor] = []
    inv[valor].append(chave)

print(15*"-")
print(inv)
