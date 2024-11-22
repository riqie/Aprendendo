'''
Crie uma classe chamada Employee que inclui três variáveis de instância: um nome
(string), um sobrenome (string) e um salário mensal (float). Sua classe deve ter um
construtor que inicializa as três variáveis. Forneça um método get e set para cada
variável. Se o salário mensal fornecido pelo usuário não for positivo, configure-o
como 0.0. Teste a classe implementada e seus métodos. Crie dois objetos Employee e
exiba o salário anual de cada objeto. Depois, dê 10% de aumento para cada
empregado e exiba novamente os salários.
'''

class Employee():
    '''atributos'''
    def __init__(self, nome, sobrenome, salario):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__verificar_salario_negativo(salario)
    
    '''metodo adicionado'''
    def __verificar_salario_negativo(self, salario):
        if salario < 0:
            salario = 0 
        self.__salario = salario

    '''metodos'''
    def mostrar_funcionario(self):
        return f'\nName: {self.__nome}\nSurname: {self.__sobrenome}\nSalary: {self.__salario}'

    def getNome(self):
        return self.name
    
    def setNome(self, name):
        self.name = name

    def getSobrenome(self):
        return self.__sobrenome

    def setSobrenome(self, sobrenome):
        self.__sobrenome = sobrenome

    def getSalario(self):
        return self.__salario

    def setSalario(self,salario):
        self.__verificar_salario_negativo(salario)

    def getSalarioAnual(self):
        return self.__salario * 12
    
    def setAumento(self, porcentagem):
        self.__salario += self.__salario * porcentagem/100

