'''
O número 3025 possui a interessante característica:
30 + 25 = 55
55² = 3025
Faça um programa que procure todos os números de 4 algorítmos que possuem essa característia.
'''

numero_separado = []
numero = input('Digite um número: ')

numero_separado.append(list(numero[0:2]))
numero_separado.append(list(numero[2:4]))

valor1= numero_separado[0]
valor2= numero_separado[1]

print(valor1, valor2)

