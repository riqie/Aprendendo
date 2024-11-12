'''
3. Crie uma classe chamada VendingMachine que simule uma máquina de venda de
produtos. Essa classe deve permitir cadastrar produtos, selecionar um produto para
compra, inserir dinheiro, retornar o troco e exibir o estoque disponível.
'''

from vendingmachine import VendingMachine

def main():
    # cadastra o produto
    vending_machine = VendingMachine()
    product1 = VendingMachine.create_product("Refrigerante", 5.0, 10)
    product2 = VendingMachine.create_product("Chips", 3.0, 5)
    print()

    # adiciona o produto cadastrado na maquina
    vending_machine.add_product(product1)
    vending_machine.add_product(product2)
    print(vending_machine.display_stock())
    print()
    
    # insere o dinheiro
    print(vending_machine.insert_money(10))

    # mostra o preço do produto
    price = vending_machine.select_product("Refrigerante")

    if isinstance(price, str):
        print(price)
    else:
        print(f"Preço do produto: R${price:.2f}")

    # mostra o troco e passa como parametro o produto quer vai comprar
    print(vending_machine.return_change('Chips'))

main()
