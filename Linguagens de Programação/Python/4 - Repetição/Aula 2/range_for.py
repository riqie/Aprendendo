#exemplos de range e for usados juntos!

for i in list(range(10)):
    print("Isso sera escrito 10 vezes")
    
n = int(input("Entre com um numero positivo: "))
for i in range(n):
    print("isso sera escrito", n, "vezes")

a = int(input("Entre com um numero positivo: "))
for i in range(1, a+1):
    print(i)
print("fim")

