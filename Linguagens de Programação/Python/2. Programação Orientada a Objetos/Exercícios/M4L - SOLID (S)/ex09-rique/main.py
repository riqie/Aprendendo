'''
9. Crie uma classe chamada Date que inclui três variáveis de instância: dia (int), mês
(int) e ano (int). Sua classe deve ter um construtor que inicializa as três variáveis de
instância e assume que os valores fornecidos são corretos. Forneça um método get e
um set para cada variável. Forneça um método que exibe o dia, o mês e o ano
separados por barras “/”. Teste a classe implementada e seus métodos.
'''



from new_date import Date

def main():
    data = Date('9', 9, 2024)

    print("Data inicial:", data.exibir_data())

    print("Dia:", data.get_dia())
    print("Mês:", data.get_mes())
    print("Ano:", data.get_ano())

    data.set_dia(10)
    data.set_mes(10)
    data.set_ano(2025)

    print("Nova data:", data.exibir_data())


main()
