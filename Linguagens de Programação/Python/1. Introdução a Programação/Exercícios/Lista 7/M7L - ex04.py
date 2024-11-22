'''
Escreva um programa que conta todas as vogais presentes no texto recebido como 
parâmetro e retorna um dicionário contendo a quantidade de cada vogal. Seu 
programa deve exibir, no fim, os dados do dicionário retornado
'''

print('='*50)
print('Iniciando o CountVogal...')
print('O programa irá ler as vogais fornecidas, \ndepois fará a contagem e a separação das mesmas em um dicionário.')
print('='*50)


dicionariogg = {}
vogais = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
frase = input('Escreva uma frase: ')

print('='*50)

# aqui é feita a contagem das letras, uma por uma.
for letra in frase: 

    # aqui verifica se a letra está entre as vogais,
    # caso não esteja é 'falso' e continuará para próxima letra da frase.     
    if letra in vogais:
        
        # esta condição sempre inicia como 'falsa',
        # então ela cai no 'else' e adiciona a primeira vogal,
        # caso a vogal se repita, ela é somada.
        if letra.lower() in dicionariogg:
            dicionariogg[letra.lower()] += 1

        else:
            dicionariogg[letra.lower()] = 1


print('Dicionário de vogais e suas contagens:')
print(dicionariogg)

print('='*50)

print('Fim gg')
