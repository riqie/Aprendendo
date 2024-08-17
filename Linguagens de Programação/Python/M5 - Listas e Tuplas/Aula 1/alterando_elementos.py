# Alterando um item da lista

companies= list(['toyota', 'Volkswagen', 'ford'])
print(companies)

companies[2]= "Google"
print(companies)

# Alterando um trecho da lista

list = [0, 1, 2, 3, 4, 5]
list[2:4] = ["A", "B"]
print(list)


list[2:4] = [8, 8, 8]
print(list)


list[4:6] = []
print(list)

