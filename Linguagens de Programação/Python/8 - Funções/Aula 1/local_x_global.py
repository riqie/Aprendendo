#A local "esconde" a global

a = 1

def printVariable():
	a = 5
	print(a)

printVariable()
print(a)
