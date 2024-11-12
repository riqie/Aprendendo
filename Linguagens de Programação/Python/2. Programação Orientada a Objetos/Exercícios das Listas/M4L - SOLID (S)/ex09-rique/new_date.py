'''
9. Crie uma classe chamada Date que inclui três variáveis de instância: dia (int), mês
(int) e ano (int). Sua classe deve ter um construtor que inicializa as três variáveis de
instância e assume que os valores fornecidos são corretos. Forneça um método get e
um set para cada variável. Forneça um método que exibe o dia, o mês e o ano
separados por barras “/”. Teste a classe implementada e seus métodos.
'''

class Date:
    '''atributos'''
    def __init__(self, dia: int, mes: int, ano: int):
        self._dia = dia
        self._mes = mes
        self._ano = ano

    '''metodos'''
    def exibir_data(self):
        return f"{self._dia:02}/{self._mes:02}/{self._ano}"
    
    def get_dia(self):
        return self._dia

    def get_mes(self):
        return self._mes

    def get_ano(self):
        return self._ano

    def set_dia(self, dia: int):
        self._dia = dia

    def set_mes(self, mes: int):
        self._mes = mes
 
    def set_ano(self, ano: int):
        self._ano = ano


