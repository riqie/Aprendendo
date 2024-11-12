'''Crie uma classe Invoice para que uma loja de suprimentos de informática possa
utilizá-la para representar a fatura de um item vendido na loja. Uma Invoice deve
incluir quatro variáveis de instância: o número da fatura (string), a descrição (string),
a quantidade comprada de um item (int) e o preço por item (float). Sua classe deve ter
um construtor que inicializa as quatro variáveis de instância. Forneça um método set
e um get para cada variável de instância. Forneça também um método chamado que
calcula o valor da fatura (multiplica preço por quantidade do item) e retorna o
resultado. Se a quantidade de itens passada pelo usuário não for positiva, deve ser
configurada como 0. Se o preço do item não for positivo, deve ser configurado como
0.0. Teste a classe implementada e seus métodos.'''

class Invoice:
    # o atributo privado nao tem como ser alterado fora da classe sem um metodo
    def __init__(self,n_invoice,description,quantity=0,price=0):
        
        if price >= 0:
            self._price = price
        else:
            self._price = 0.0
            
        self._n_invoice = n_invoice
        self._description = description

        if quantity >= 0:
            self._quantity = quantity
        else:
            self._quantity = 0
            
    def getN_invoice(self):
        return self._n_invoice
    
    def getDescription(self):
        return self._description
    
    def getQuantity(self):
        return self._quantity
    
    def getPrice(self):
        return self._price
    
    def setN_invoice(self, valor):
        self._n_invoice = valor
    
    def setDescription(self,new_description):
        self._description = new_description
    
    def setQuantity(self,quantity):
        self._quantity = quantity
    
    def setPrice(self,price):
        self._price = price
        
    def totalInvoice(self):
        return self._quantity * self._price
        
    
    
