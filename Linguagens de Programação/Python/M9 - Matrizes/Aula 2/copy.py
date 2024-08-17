# copiar cada linha:

A = [[1,2],[3,4]]
B = A.copy()

B[0][0]=0

print(A)
print(B)

B = [linha.copy for linha in A]
B[0][0] = 0

print(A)
print(B)

