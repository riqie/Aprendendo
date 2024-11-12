#aqui ele analisa qual elemento da string o usuário informou.

msg = "hello world"
print(msg[0])
print(msg[1])
print(msg[-1])
print(msg[-5])
print(msg[10])

# assim como as tuplas, não podemos mudar os elementos de uma string, resultando em erro, veja:

#msg[0] = "y"

#como acessar trechos de uma string: string[start:stop:step], ex:

print(msg[3:8])
print(msg[:5])
print(msg[6:])
print(msg[::2])
print(msg[::-1])
print(msg[0:10:3])


