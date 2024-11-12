""""6. Implemente uma classe chamada Library que represente uma biblioteca virtual. Essa
classe deve permitir cadastrar livros, fazer empréstimos, devolver livros e verificar a
disponibilidade de um livro."""

from library import Library

livraria = Library()
livraria.register("Pequeno Principe",3)
livraria.register("Arte da Negociação",4)
livraria.loan("Pequeno Principe",1,"Leonardo")

print(livraria.availability())
print(livraria.client())

livraria.retur("Pequeno Principe",1,"Leonardo")

print(livraria.availability())
