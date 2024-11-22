'''1. Crie uma classe chamada VirtualStore que represente uma plataforma de vendas 
online. Essa classe deve ter funcionalidades para cadastrar produtos, gerar carrinho 
de compras, aplicar descontos e calcular o valor total da compra'''

from virtualstore import VirtualStore

def main():
    VirtualStore.add_product('Laptop', 2000)
    VirtualStore.add_product('Mouse', 50)

    store = VirtualStore()
    store.add_to_cart('Laptop')
    store.add_to_cart('Mouse')

    total = store.calculate_total()
    discounted_total = VirtualStore.calculate_discount(total, 10)
    print(f"Total com desconto: {discounted_total}")
    
main()
