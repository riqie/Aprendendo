'''
Faça um programa que conta quantos caracteres únicos existem em uma string. A
string 'Hello, world!' tem dez caracteres únicos, enquanto a string 'zzz' tem apenas
um. Utilize um dicionário para resolver esse problema.
'''

contador = {}
string = input("Entre com a string desejada: ")

for caracter in string:
    if caracter not in contador:
        contador[caracter] = [caracter]

caracteres_unicos = len(contador)
if caracteres_unicos > 1:
    print(f"A string possui {caracteres_unicos} caracteres únicos!")
else:
    print(f"A string possui {caracteres_unicos} caracter único!")
