'''
Para enviar mensagens que não devem ser lidas por estranhos, pode-se codificá-las. 
Faça um programa que leia uma frase e a seguir codifique essa frase da seguinte 
forma: cada letra que se encontra em posição ímpar na tabela ASCII tem este seu 
valor ASCII dividido por 2, e cada letra que se encontra em posição par na mesma 
tabela é trocada por outra, 3 posições atrás dela da tabela. No final, imprima a frase 
codificada.
print('='*50)
print('\n O programa vai criptografar a sua frase para que estranhos não a entendam.\n')
'''

print('='*50)
frase = input('\nEscreva uma frase: ')
frase_criptografada = []

for caracter in frase:

    if caracter.isdigit():

        frase_criptografada.append(caracter)

    elif ord(caracter) % 2 == 1:

        cript_caracter = chr(int(ord(caracter) / 2))
        frase_criptografada.append(cript_caracter)

    elif caracter == ' ':

        frase_criptografada.append(caracter)
        
    else:
        
        cript_caracter = chr(ord(caracter) - 3)
        frase_criptografada.append(cript_caracter)

print('')
print(''.join(frase_criptografada))
print('='*50)
print('\nfim do programa gg')
