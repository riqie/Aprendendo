# obtendo aposição de algum item da lista, caso não esteja na lista, ocorrerá um erro:

empresas = ["Sony Pictures", "Walt Disney", "HBO", "Warner"]

a = input("COLOQUE UMA SÉRIE: ")

print(empresas.index("Warner"))
print(empresas.index("HBO"))

# Evitando o erro:

if a in empresas:
    print(empresas.index("HBO"))
else:
    print("hbo não está na lista")