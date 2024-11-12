'''Implemente uma classe chamada Schedule que represente uma agenda telefônica.
Essa classe deve permitir adicionar, editar e remover contatos, além de buscar por
contatos a partir de um nome ou número de telefone.'''

from schedule import Schedule 

def main():
    Schedule.add_book("Rafael","942186154")
    Schedule.print_list()
    Schedule.add_book("Mota","101010101")
    Schedule.print_list()
    Schedule.remove_book("Mota")
    Schedule.remove_book("Fio")
    Schedule.print_list()
    Schedule.search("Rafael")
    Schedule.edit_contact("Rafael","123456789")
    Schedule.print_list()
    
main()
