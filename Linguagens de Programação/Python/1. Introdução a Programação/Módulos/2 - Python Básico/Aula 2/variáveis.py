# Variáveis são atribuições para um tipo de comando, exemplo:
a = b = c = 3
print( a , b , c)
# Note que não foi preciso usar aspas nas devidas letras, pois elas receberam uma atribuição, elas se tornaram cada uma, uma variável.

x, y, z = 1, 2, 3
print( x , y , z)
# OBS: as variáveis devem começar por uma letra ou sublinhado.

# Python é case sensitive, ou seja, diferencia maiúsculas de minúsculas! Exemplo:
c1= 0
C1= "1"
print( c1, "o tipo desta variável é:", type(c1))
print( C1, "o tipo desta variável é:", type(C1))


IFSP = "Instituto Federal de São Paulo"
jcrprog_2024_1= "JCRPROG"
verdadeiro = True
falso = False
print(IFSP, type(IFSP))
print(jcrprog_2024_1, type(jcrprog_2024_1))
print(verdadeiro, type(verdadeiro), falso, type(falso))
