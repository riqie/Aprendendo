# matriz é uma lista de listas
# acesso por linha e coluna
# começa na posição 0

matrix = [[1,2,3], [4,5,6], [7,8,9]]
# índice:  0 1 2    0 1 2    0 1 2

print(matrix[0][2])
print(matrix[2][1])

matrix2 = [[1,2], [3,4]]
print(matrix2[0][0])
print(matrix2[1][1])

#print(matrix2[2][2])  #linha de erro!

'''

erro ao acessar posição inexistente:
matriz= [[1,2], [3,4]]
print(matriz[0][0])
print(matriz[1][1])
print(matriz[2][2])

'''