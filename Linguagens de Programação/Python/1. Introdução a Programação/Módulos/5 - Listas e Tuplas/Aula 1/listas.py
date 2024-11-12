# LISTAS:

'''
A estrutura de lista serve para armazenar múltiplos dados,
as listas podem ser chamadas de ARRAY ou VETOR.
'''
print("="*30)
print(" Para criar uma lista eu devo utilizar colchetes. Ex:") 
print("="*30)

fruits = ["Pineapple","Banaana", "Khaki", "Damascus"]
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
data = ["Carlos", 19, True, 1.78, 2001]

print(fruits)
print(numbers)
print(letters)
print(data)

print("="*30)
print(" Como fazer o uso das listas? FUNÇÃO: LIST. Ex:")
print("="*30)

a = list(range(10))
a = list()
companies= list(['toyota', 'Volkswagen', 'ford'])
ifsp = list("IFSP")

print(a)
print(companies)
print(ifsp)

print("="*30)
print(" Acesso ao i-ésimo elemento, Ex:")
print(' Utilizarei a lista "letters" criada acima')
print("="*30)

# usarei a lista 'letters' acima.
print(letters[0])
print(letters[1])
print(letters[4])

print("="*30)
print(" Agora o acesso invertido")
print("="*30)

print(letters[-1])
print(letters[-4])
