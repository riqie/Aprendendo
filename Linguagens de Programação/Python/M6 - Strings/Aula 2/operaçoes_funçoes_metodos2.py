#função split: divide uma string em uma lista de acordo com um padrao de caracteres(separador)
'''
str1 = "     JCRPROG Introduction \t\t to \n Programming      "
data = str1.split()
print(data)
str2 = "pineapple, banana, khaki, damascus"
fruits = str2.split(",")
print(fruits)
print("-"*40)

#mais exemplos, veja:
s1, s2 = input().split()
print("-"*40)
a, b, c = [int(i) for i in input().split()]
print("-"*40)
numbers = [float(i) for i in input().split()]
print("-"*40)

print(s1, "\n",s2)
print("-"*40)
print( a, b, c)
print("-"*40)
print(numbers)
'''

#função join: junta uma lista de strings, veja:
fruits = ["pineapple", "banana", "khaki", "damascus"]
txt = "==123".join(fruits)
print(txt)
