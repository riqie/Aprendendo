'''
Escreva um programa que, dada uma String representando um texto, imprima o
número de palavras existentes. Observação: você deve remover os sinais de
pontuação (“.”, “,”, “:”, “;”, “!” e “?”) antes de realizar a contagem das palavras.
'''

print("Programa para realizar a contagem de palavras.")
texto = str(input("Insira um trecho de texto: \n"))

#removendo os sinais de pontuação

a = texto.replace(",","")
b = a.replace(".","")
c = b.replace(";","")
d = c.replace(":","")
e = d.replace("!","")
f = e.replace("?","")
#print(f)

#contando as palavras
lista = f.split()
#print(lista)
print("A quantidade de palavras dentro do trecho é", len(lista))
