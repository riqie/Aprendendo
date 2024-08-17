exemplo = {
    'fruta': 'banana',
    'carro': 'gol',
    'cor': 'purple',
    'nome': 'henrique',
    'telefone': '128718977'
}

# iterando chaves:
for chave in exemplo.keys():
    print('Chaves:', chave)

# iterando valores:
for valor in exemplo.values():
    print('Valor:', valor)

# iterando itens:
exemplo2 = {
    'a': 'abacate',
    'b': 'banana',
    'c': 'caqui'
}

for (letra, fruta) in exemplo2.items():
    print('fruta com a letra ', letra, ': ', fruta, sep='')





