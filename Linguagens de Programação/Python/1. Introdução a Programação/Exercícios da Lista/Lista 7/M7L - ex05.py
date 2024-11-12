'''
A conta do cartão de crédito de uma pessoa pode ser modelada por um dicionário
com os campos saldo, com o saldo devedor da conta, transações, com o número de
transações que gerou esse saldo, e média, com a média de gastos por transação. O
programa deve preencher o dicionário com a conta e o valor da compra e gerar um
novo dicionário para aquela conta, com o saldo devedor, número de transações e
média de gastos atualizados.
'''

print('Conta bancária')
print('Informe o saldo devedor da conta, e quantas compras foram realizadas')
saldo = float(input('Qual o saldo devedor: '))
qnt = float(input('Quantas compras foram realizadas: '))
media = saldo / qnt
dados = {
    'Saldo' : saldo, 'Quantidade' : qnt, 'Media de gastos' : media
}
print(f'Informações gerais \n {dados}')
