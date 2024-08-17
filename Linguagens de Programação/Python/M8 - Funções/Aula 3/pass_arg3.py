def duplicarLista(lista):
  lista.append(lista[-1])
  print(lista)

numeros = [1,2,3,4]
duplicarLista(numeros.copy())
print(numeros)