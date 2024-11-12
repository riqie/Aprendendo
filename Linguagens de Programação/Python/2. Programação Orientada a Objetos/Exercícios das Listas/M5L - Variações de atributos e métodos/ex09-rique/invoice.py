'''
9. Crie uma classe chamada Invoice que possa ser utilizado por uma loja de
suprimentos de informática para representar uma fatura de um item vendido na loja.
Uma fatura deve incluir as seguintes informações como atributos:
• o número do item faturado,
• a descrição do item,
• a quantidade comprada do item e
• o preço unitário do item.
Sua classe deve ter um construtor que inicialize os quatro atributos. Se a quantidade
não for positiva, ela deve ser configurada como 0. Se o preço por item não for
positivo ele deve ser configurado como 0.0. Forneça um método set e um método get
para cada variável de instância. Além disso, forneça um método chamado que calcula
o valor da fatura (isso é, multiplica a quantidade pelo preço por item) e depois retorna
o valor real. Escreva um aplicativo de teste que demonstra as capacidades da classe
Invoice.
'''
class Invoice:
    def __init__(self, number, description, quantity, price):
        self.__number = number
        self.__description = description
        self.__quantity = self.__verify_quantity(quantity)
        self.__price = self.__verify_price(price)

    def __verify_quantity(self, quantity):
        if quantity > 0: 
            return quantity 
        return 0


    def __verify_price(self, price):
        return price if price > 0 else 0.0

    # Getters e Setters
    def get_number(self):
        return self.__number

    def set_number(self, number):
        self.__number = number

    def get_description(self):
        return self.__description

    def set_description(self, description):
        self.__description = description

    def get_quantity(self):
        return self.__quantity

    def set_quantity(self, quantity):
        self.__quantity = self.__verify_quantity(quantity)

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = self.__verify_price(price)

    def get_invoice_amount(self):
        return self.__quantity * self.__price

    @classmethod
    def from_values(cls, number, description, quantity, price):
        return cls(number, description, quantity, price)

    @staticmethod
    def calculate_total(amounts):
        return sum(amounts)
