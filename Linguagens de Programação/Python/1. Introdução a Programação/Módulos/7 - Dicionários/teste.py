def calcularCustoTotal(lista_livros, CUSTO_FIXO, LUCRO):
    """
    Calcula o custo total de produção de uma lista de livros e retorna:
    - lista_livros atualizada com custos e preços
    - preço médio de venda com lucro
    - quantidade total de livros
    """
    quantidade_total_livros = 0
    valor_venda_total = 0

    for dicionario in lista_livros:
        # Cálculo do custo total de produção de um livro (páginas + encadernação) por cópia
        custo_por_copia = dicionario['Valor das Páginas'] + dicionario['Valor de Encadernação']
        custo_livros = dicionario['Cópias'] * custo_por_copia
        dicionario['Custo Livros'] = custo_livros

        # Somar o custo fixo total distribuído
        custo_producao = CUSTO_FIXO + custo_livros
        dicionario['Custo Produção'] = custo_producao

        quantidade_total_livros += dicionario['Cópias']
        valor_venda_total += dicionario['Valor de Venda'] * dicionario['Cópias']

    # Cálculo do valor de venda total com lucro de 20%
    valor_venda_com_lucro = valor_venda_total * LUCRO
    preco_medio_livro = valor_venda_com_lucro / quantidade_total_livros

    return lista_livros, preco_medio_livro


def obterTipoEncadernacao():
    """
    Determinar o valor da encadernação com base no input do usuário.
    """
    while True:
        tipo_encadernacao = input('Qual tipo de encadernação deseja?\n[1] - SIMPLES: R$4,30\n[2] - ESPECIAL: R$7,80\n[3] - LUXO: R$10,50\n: ')
        if tipo_encadernacao == '1':
            return 4.30
        elif tipo_encadernacao == '2':
            return 7.80
        elif tipo_encadernacao == '3':
            return 10.50
        else:
            print('Opção inválida. Tente novamente.')


def criarLivro(CUSTO_POR_PAGINA):
    """
    Cria uma lista de livros a partir da entrada do usuário, incluindo
    o número de páginas, tipo de encadernação e o número de cópias vendidas.
    """
    lista_livros = []
    
    # Validação do número de livros
    while True:
        try:
            quantidade_livros = int(input('Digite o número de livros diferentes: '))
            if quantidade_livros > 0:
                break
            else:
                print('A quantidade de livros deve ser positiva.')
        except ValueError:
            print('Valor inválido. Por favor, insira um número inteiro.')

    for i in range(quantidade_livros):
        print(f'\nLivro {i+1}:')

        # Validação da quantidade de páginas
        while True:
            try:
                quantidade_paginas = int(input(f'Quantas páginas o livro {i+1} terá? '))
                if quantidade_paginas > 0:
                    break
                else:
                    print('O número de páginas deve ser positivo.')
            except ValueError:
                print('Valor inválido. Por favor, insira um número inteiro.')

        tipo_encadernacao = obterTipoEncadernacao()

        # Validação do valor do livro
        while True:
            try:
                valor_livro = float(input('Qual o valor do livro? '))
                if valor_livro > 0:
                    break
                else:
                    print('O valor do livro deve ser positivo.')
            except ValueError:
                print('Valor inválido. Por favor, insira um número válido.')

        # Validação da quantidade de cópias
        while True:
            try:
                livros_vendidos = int(input('Quantas cópias serão feitas? '))
                if livros_vendidos > 0:
                    break
                else:
                    print('A quantidade de cópias deve ser positiva.')
            except ValueError:
                print('Valor inválido. Por favor, insira um número inteiro.')

        # Criação do dicionário para o livro
        livro = {
            'Valor das Páginas': quantidade_paginas * CUSTO_POR_PAGINA,
            'Valor de Encadernação': tipo_encadernacao,
            'Valor de Venda': valor_livro,
            'Cópias': livros_vendidos
        }

        lista_livros.append(livro)

    return lista_livros


def imprimirDados(lista_livros, preco_medio_livro):
    print('\nB. Total de livros analisados:')
    print(len(lista_livros))

    print('\nC. Preço médio de venda dos livros (com lucro de 20%):')
    print(f'R$ {preco_medio_livro:.2f}')

    # Coleta dos preços de venda dos livros
    precos_venda = [livro['Valor de Venda'] for livro in lista_livros]

    print('\nD. Preço de venda dos livros mais barato e mais caro:')
    print(f'Mais barato: R$ {min(precos_venda):.2f}')
    print(f'Mais caro: R$ {max(precos_venda):.2f}')


def main():
    CUSTO_FIXO = 4397.00
    CUSTO_POR_PAGINA = 0.03
    LUCRO = 1.2

    lista = criarLivro(CUSTO_POR_PAGINA)
    lista_livros, preco_medio_livro = calcularCustoTotal(lista, CUSTO_FIXO, LUCRO)
    imprimirDados(lista_livros, preco_medio_livro)

main()
