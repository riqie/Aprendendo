# Para fazer o balanço mensal de um armazém, faça um programa que que leia para um 
# número qualquer de mercadorias diferentes o preço de custo, o preço de venda e a 
# quantidade vendida. A partir desses dados imprima: o número total de mercadorias 
# diferentes lidas, o faturamento total e o lucro total do armazém.

def inserirMercadorias():
    mercadorias = []

    while True:
        nome = input('Digite o nome da mercadoria: ')

        if nome == '':
            return mercadorias
        
        custo = input('Digite o preço de custo da mercadoria: ')
        venda = input('Digite o preço de venda da mercadoria ')
        quantidade = input('Digite a quantidade dessa mercadoria: ')
        vendidos = input('Digite a quantidade que foi vendida: ')

        # if custo.isalpha() or venda.isalpha() or quantidade.isalpha() or vendidos.isalpha():
        #     print('Algum dos itens não possui entrada válida para a leitura, entre novamente com os dados.')
        #     continue

        # custo, venda, quantidade, vendidos = int(custo), int(venda), int(quantidade), int(vendidos)

        # if vendidos > quantidade:
        #     print('A quantidade de vendas não corresponde á quantidade de mercadorias obtidas.')
        #     continue

        mercadorias.append({
            'Mercadoria': nome,
            'Valor de custo': custo,
            'Valor de venda': venda,
            'Quantidade': quantidade,
            'Vendidos': vendidos
            })
        
        for item in mercadorias:
            for valores in item.values():    
                if valores == '':
                    print('Uma ou mais de suas entradas são inválidas, tente novamente.')
                    continue
    
def gestaoCaixa(mercadorias):
    totalFaturamento = 0
    lucroTotal = 0

    for item in mercadorias:
        mercadoriasUnicas = len(mercadorias)
        totalFaturamento += item['Valor de venda'] * item['Vendidos']
        lucroTotal += (item['Valor de venda'] * item['Vendidos']) - (item['Valor de custo'] * item['Quantidade'])

    return totalFaturamento, lucroTotal, mercadoriasUnicas

def main():
    print('O programa fará o balanço mensal de um armazém. Para isso digite a mercadoria, a quantidade, o preço de custo, o preço de venda e a quantidade vendida\nDeixe em branco para parar de colocar mercadorias.\n')
    
    mercadorias = inserirMercadorias() 
    # totalFaturamento, lucroTotal, mercadoriasUnicas = gestaoCaixa(mercadorias)
    # print('\nResultado da gestão:\n')
    # print(f'\n- Faturamento Total: {totalFaturamento:.2f} R$\n- Lucro Total: {lucroTotal:.2f} R$\n- Mercadorias Diferentes: {mercadoriasUnicas}.')
    # print('\nfim do programa')

main()
# falta arrumar muita coisa na função inserir mercadorias, obs: criar uma outra função para corrigir o erro de inputs.
