#ubstituit todos os caracters de uma string or outros, veja:
x = "introduction to programming"
y = x.replace("o","_")
print(y)
y = x.replace("introduction", "$"*len("introduction"))
print(y)
x = "a,b,c,d,e"
y = x.replace(",", "")
print(y)
