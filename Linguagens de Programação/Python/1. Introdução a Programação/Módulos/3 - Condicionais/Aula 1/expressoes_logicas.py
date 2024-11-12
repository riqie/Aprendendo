# expressoes que realizam uma operação baseada em logica e retornam um valor de verdadeiro ou falso.
# operadores lógicos: and ou &, or ou | e not.
'''
True and True = True
True and False = False
False and False = False

True or True = True
True or False = True
False or False = False
'''

a = 10
b = 20

#operadores and:
# resultado será verdadeiro quando ambas forem verdadeiras, caso contrário, serás falso.

print(a == 10 and b == 20)
print(a == 11219302489 and b == 20)
print(a == 10 and b == 89419834)
print(a == 10 and b == 204)
print("-"*30)

#------ operador or, será verdadeiro quando pelo menos 1 dos dois for verdadeiro, caso contrario, será falso:

print(a == 10 or b == 20)
print(a == 32342 or b == 20)
print(a == 10 or b == 34234)
print(a == 31232 or b == 12) 
print("-"*30)

# ------ operador not, inverterá o valor booleano, ou seja, caso fosse verdadeiro, será falso, caso contrário, será verdadeiro:

print(not(a == 10)) #verdade
print(not(a == 1082108)) #mentira
print(not(b == 20))# verdade
print(not(b == 1398294829))#mentira