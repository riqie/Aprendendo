#este comando irá repetir todos os valores de uma lista, ate que seja falso. Veja:

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
i = 0

for letra in letras: #aqui podemos criar uma variável após digitar for!
    print(letra)

#funciona como um while, porém bem mais simplificado.
print("="*40)
# obtendo o max usando for, veja:

numeros = [3, 4, 45, 6, 7, 8]
maxi = numeros[0]
for numero in numeros:
    if numero > maxi:
        maxi = numero
print(maxi)
