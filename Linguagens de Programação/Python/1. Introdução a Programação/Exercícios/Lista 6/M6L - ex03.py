# Um palíndromo é uma palavra ou frase que pode ser lida da mesma forma tanto da 
# esquerda para a direita como da direita para a esquerda (desconsiderando os 
# espaços em branco). Considere que a entrada não possui sinais de pontuação ou 
# acentos. Escreva um programa que, dada uma String, verifique se ela é um 
# palíndromo

print('\nEste programa informa se a frase digitada é uma palíndromo ou não.\nPalíndromo: frases ou plavras que ao escreve-las de trás para frente seu sentido permanece.Ex: Ovo, Roma me tem amor...\n',('='*50))

frase = str(input('\nEscreva uma frase ou palavra: ')).lower()

frase_invertida = frase[::-1]
frase = frase.split()
frase_invertida = frase_invertida.split()


print(frase)
print(frase_invertida)
print('-'*30)

if ''.join(frase) == ''.join(frase_invertida):
    print('Esta frase é um palindromo.')

else:
    print('Esta frase não corresponde a um palíndromo.')

print('')
print('='*50)
print('\nFim do programa gg')
