msg = "hello"
msg2 = "y" + msg[1:] + "w"
print(msg2)
print("-"*40)

s = "abc"
print(s*3)
print("-"*40)

#tamanho de uma string:
print(len(msg))
msg2 = "hello world"
print(len(msg2))
msg3 = "hello\nworld"
print(len(msg3))
print("-"*40)

#comparação de strings:
a = "python"
b = "py" + "thon"
c = "p" + "ython"
print(a == b)
print(a == c)
print(b != c)
print("-"*40)

print("thon" in "python")
print("thor" in "python")
msg = "hello world"
print(msg.startswith("hello"))
print(msg.startswith("hello"))
print("-"*40)

# buscando uma string: (index)
bond = "my name is Bond, James Bond"
print(bond.index("Bond"))
msg = "hello world"
print(msg.index("world"))
print("-"*40)

# print(msg.index("bond")) #erro

# agora, buscando uma string: (find)
print(bond.find("Bond"))
print(msg.find("hello"))
print(msg.find("hello")) #-1
print("-"*40)

#manipulando uma string: (strip)
#remove todos os espaços em branco (incluindo quebras de linhas).
MSG = "\n hello world\t"
print(MSG.strip())
print("-"*40)



