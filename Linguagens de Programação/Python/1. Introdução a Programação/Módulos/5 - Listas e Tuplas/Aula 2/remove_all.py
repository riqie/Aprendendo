# removendo todos os itens da lista:

n = int(input(" Quantos números serão lidos? "))
lista = []

for i in range(n):
    lista.append(int(input()))

x = int(input("qual numero remover?"))

while x in lista:
    lista.remove(x)
print(lista)


'''for qualquecoisa in range(len(lista)):
    lista.remove(x)
print(lista)
'''


