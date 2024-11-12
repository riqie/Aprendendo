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

from invoice import Invoice

def creat_object():
    invoice1 = Invoice(1423, "Teclado", 2, 150.0)
    invoice2 = Invoice(2665, "Mouse", 0, 80.0)  # quantidade não positiva
    invoice3 = Invoice(3126, "Monitor", 1, -300.0)  # preço não positivo
    invoices = [invoice1, invoice2, invoice3]

    amounts = []
    for invoice in invoices:
        amount = invoice.get_invoice_amount()
        amounts.append(amount)

    return invoices, amounts

def main(): 
    list_invoices, amounts = creat_object()
    invoice1 = list_invoices[0]
    invoice2 = list_invoices[1]
    invoice3 = list_invoices[2]

    print(f"Fatura 1:\n{invoice1.get_description()}, Valor: {invoice1.get_invoice_amount()}\n")
    print(f"Fatura 2:\n{invoice2.get_description()}, Valor: {invoice2.get_invoice_amount()}\n")
    print(f"Fatura 3:\n{invoice3.get_description()}, Valor: {invoice3.get_invoice_amount()}\n")
    
    total_amount = Invoice.calculate_total(amounts)
    print(f"Valor total das faturas: {total_amount}")


main()
