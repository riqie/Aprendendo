
class Library:

    __books = {}
    __loans = {}
    
    @classmethod
    def register(cls,book,availability):
        print("Registering...")
        cls.__books[book] = availability

    @classmethod
    def loan(cls,book,quantity,name):
        if book in cls.__books:
            cls.__books[book] -= quantity
            cls.__loans[name] = book
            cls.printe_loan(book)
            
    @classmethod
    def retur(cls,book,quantity,name):
        if book in cls.__books:
            cls.__books[book] += quantity
            del cls.__loans[name]
            cls.printe_retur(book)
            
    @classmethod
    def availability(cls):
        return f"Availability:\n{cls.__books}"
    
    @classmethod
    def client(cls):
        return f"Clients:\n{cls.__loans}"
    
    @classmethod
    def printe_loan(cls,book):
         print("Lending...")
         print(f"Disponibilidade do livro {book}:{cls.__books[book]}")
         print("Sucessful")
         
    @classmethod
    def  printe_retur(cls,book): 
        print("Returning...")
        print(f"Disponibilidade do livro {book}:{cls.__books[book]}")
        print("Sucessful") 
    
        
    
    
