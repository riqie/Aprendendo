'''
Exercício 1
Faça um programa que leia uma frase, e duas letras quaisquer do usuário. A seguir, troque na frase todas as ocorrências da primeira letra fornecida pela segunda e imprima a nova frase
'''

frase = str(input('Digite uma frase:'))
print(50*"-")

l1 = str(input('Informe a letra a ser retirada:')).upper()
l1_1 = l1.lower()

l2 = str(input('Informe a letra que substituira a letra retirada:')).upper()
l2_2 = l2.lower()
print(50*"-")

frase_nova = frase.replace(l1,l2) #Substituição das maiúsculas
frase_nova = frase_nova.replace(l1_1,l2_2) #Substituição das minúsculas

print(f'Nova frase = {frase_nova}')
