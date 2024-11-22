'''
Exercício 5
Crie um programa que leia uma frase e, a seguir, imprima: 
a. Quantos caracteres foram digitados.
b. Quantos espaços brancos existem na frase.
c. Quantos desses caracteres são minúsculos e quantos são maiúsculos.
d. Quantos desses caracteres são dígitos.
e. Quantos desses caracteres são de pontuação
'''
carac_pont = ['!','"','#','$','%','&',"'",'(',')','*','+',',','-','.','/',':',';','<','=','>','?','@','[','\\',']','^','_','`','{','|','}','~']
frase = str(input('Informe uma frase:'))
vazios = frase.count(' ')
num_letras = len(frase) - vazios
print(f'A) Número de caracteres na frase = {num_letras}')
print(f'B) Número de espaços brancos na frase = {vazios}')
l = u = n = p = 0
for letras in frase:
    if letras.islower():
        l = l + 1
    elif letras.isupper():
        u = u + 1
    elif letras.isnumeric():
        n = n + 1
    elif letras in carac_pont:
        p = p + 1
print(f'C) Número de minúsculas = {l}; Número de maiúsculas = {u}')
print(f'D) Número de dígitos = {n}')
print(f'E) Número de caracteres de pontuação = {p}')
