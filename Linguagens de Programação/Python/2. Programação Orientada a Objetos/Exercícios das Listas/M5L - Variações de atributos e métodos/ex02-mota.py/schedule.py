'''Implemente uma classe chamada Schedule que represente uma agenda telefônica.
Essa classe deve permitir adicionar, editar e remover contatos, além de buscar por
contatos a partir de um nome ou número de telefone.'''

class Schedule:
    phone_book = {}
    
    @classmethod
    def add_book(cls,name,number):
        cls.phone_book[name] = number
        
    @classmethod
    def remove_book(cls,name):
        if name in cls.phone_book:
            del cls.phone_book[name]
        else:
            print('Not found.')
        
    @classmethod
    def edit_contact(cls, name, new_number):
        if name in cls.phone_book:
            cls.phone_book[name] = new_number
        else:
            print('Not found.')
        
    @classmethod
    def search(cls,name):
        return cls.phone_book[name]
    
    @classmethod
    def print_list(cls):
        print(cls.phone_book)
