# ordenamento de listas, ordenar a lista de forma crescente ou decrescente. (por padrão ele ordena crescentemente)

a = [5,3,1,4,2,6]

a.sort()
print(a)

a.reverse()
print(a)

# agora, usando o sorted:


b = sorted(a) 
print(b)

print(b[::-2])

c = ['mamao', 'banana', 'abacate', 'maça']

d = sorted(c)
print(d)

print(c)

c.sort()
print(c)