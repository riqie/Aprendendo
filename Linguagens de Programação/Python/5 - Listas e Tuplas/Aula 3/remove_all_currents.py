# removendo todas as ocorrencias:

n = int(input(" Quantos números serão lidos? "))
list = []

for i in range(n):
    list.append(int(input()))

x = int(input("Wich number should be removed? "))
c = list.count(x)

for i in range(c):
    list.remove(x)

print(list)


