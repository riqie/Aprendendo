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

from invoice import Invoice

def main():
    invoice = Invoice(245, 'white phone', 2, 450)

    print(
        invoice.getN_invoice(),
        invoice.getDescription(),
        invoice.getPrice(),
        invoice.getQuantity(),
        invoice.totalInvoice()
    )

main()
