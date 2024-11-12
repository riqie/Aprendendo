'''
3. Crie uma classe chamada VendingMachine que simule uma máquina de venda de
produtos. Essa classe deve permitir cadastrar produtos, selecionar um produto para
compra, inserir dinheiro, retornar o troco e exibir o estoque disponível.
'''

class VendingMachine:
    def __init__(self):
        self.products = {}
        self.balance = 0.0

    @classmethod
    def create_product(cls, name, price, quantity):
        return {'name': name, 'price': price, 'quantity': quantity}

    def add_product(self, product):
        name = product['name']
        if name in self.products:
            self.products[name]['quantity'] += product['quantity']
        else:
            self.products[name] = product

    def select_product(self, name):
        if name not in self.products:
            return "Produto não disponível."
        if self.products[name]['quantity'] <= 0:
            return "Produto esgotado."
        return self.products[name]['price']

    def insert_money(self, amount):
        if amount <= 0:
            return "Valor inválido."
        self.balance += amount
        return f"Você inseriu R${amount:.2f}. Saldo atual: R${self.balance:.2f}"

    def return_change(self, name):
        change = self.balance - self.products[name]['price']
        return f"Seu troco é R${change:.2f}."

    def display_stock(self):
        stock_list = []
        for name, details in self.products.items():
            stock_list.append(f"{name}: R${details['price']:.2f} (Quantidade: {details['quantity']})")
            
        if stock_list:
            return "\n".join(stock_list)
        else:
            return f"Estoque vazio."  


