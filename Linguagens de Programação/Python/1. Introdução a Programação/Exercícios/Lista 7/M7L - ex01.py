'''
Exercício 1.
Escreva um programa que recebe como entrada um número inteiro n. Em seguida, 
seu programa deve receber as informações de n Pokémon (nome, tipo e ataque). Para 
cada Pokémon seu programa deve armazenar as informações utilizando uma 
estrutura de dicionário. No fim, seu programa deve imprimir o nome do Pokémon do 
tipo “Fogo” com maior ataque. Você pode assumir que os valores de ataque são 
inteiros positivos distintos e que pelo menos um Pokémon do tipo “Fogo” será 
fornecido.
Exemplo de entrada:
4
Bulbasaur Planta 78
Charmander Fogo 83
Squirtle Água 87
Vulpix Fogo 72
Resposta:
Charmander
'''

n = int(input("Serão informados quantos pokemons(n)? "))

pokemons = {}
maior_ataque = 0
maior_nome = ""

for c in range(n):
    print(20*'-')
    nome = str(input('Nome:')).capitalize().strip()
    tipo = str(input('Tipo:')).capitalize().strip()
    ataque = int(input('Ataque:'))

    pokemons[nome] = {'tipo': tipo, 'ataque':ataque}
    
for chave, valor in pokemons.items():
    if valor['tipo'] == 'Fogo' and valor['ataque'] > maior_ataque:
        maior_ataque = valor['ataque']
        maior_nome = chave

print(20*'-')
print(f"O pokemon de fogo com maior ataque é: {maior_nome}")