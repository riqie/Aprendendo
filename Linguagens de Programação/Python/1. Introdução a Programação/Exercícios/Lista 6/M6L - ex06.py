'''
Faça um programa que leia uma frase e inverta todas as letras maiúsculas para
minúsculas e vice-versa. Além disso, o programa deve colocar um hífen no lugar de
todos os espaços em branco.
'''

print("Programa para manipular uma string")
print("Vamos inverter o tamanho das letras e adicionar um hífen entre as palavras!")
print("Maiúsculas ficam minúsculas e vice-versa!")
texto = str(input("Insira o texto: \n"))
texto1 = ""

#invertendo os tamanhos
for letra in texto:
    if letra.isupper():
        texto1 = texto1 + letra.lower()
    elif letra.islower():
        texto1 = texto1 + letra.upper()
    elif letra.isspace():
        texto1 = texto1 + "-"
    else:
        texto1 = texto1 + letra


print("-"*80)
print("frase original:")
print(texto)
print("-"*80)
print("frase modificada:")
print(texto1)
