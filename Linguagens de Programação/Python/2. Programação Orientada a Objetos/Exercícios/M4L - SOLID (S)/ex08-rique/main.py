'''
Crie uma classe chamada Employee que inclui três variáveis de instância: um nome
(string), um sobrenome (string) e um salário mensal (float). Sua classe deve ter um
construtor que inicializa as três variáveis. Forneça um método get e set para cada
variável. Se o salário mensal fornecido pelo usuário não for positivo, configure-o
como 0.0. Teste a classe implementada e seus métodos. Crie dois objetos Employee e
exiba o salário anual de cada objeto. Depois, dê 10% de aumento para cada
empregado e exiba novamente os salários.
'''

from new_employee import Employee

def main():
    print('\nO programa fará o registro de 2 funcionários, depois a mudança de 1 deles.\n')

    '''passando os dados para a classe'''
    empregado1 = Employee('Rafael ', 'Mota ', 1000)
    empregado2 = Employee('Leonardo ','Oliveira ', 2500)

    '''enunciado'''
    print(f'Objetos da Classe:\n\nFuncionario 1: {empregado1.mostrar_funcionario()}\n\nFuncionario 2: {empregado2.mostrar_funcionario()}')
    print(f'\nSalários Anuais:\nFunc1: {empregado1.getSalarioAnual()}\nFunc2: {empregado2.getSalarioAnual()}')

    '''realizando o aumento do salario'''
    empregado1.setAumento(1) # ---> aumento de 10%
    empregado2.setAumento(0.1)
    print(f'\nSalários Anuais após aumento:\nFunc1: {empregado1.getSalarioAnual()}\nFunc2: {empregado2.getSalarioAnual()}')

    '''teste dos métodos da classe'''
    # print('\nFuncionamento dos métodos para o funcionario 1: ')
    # print('=== Funcionamento do método Aumento: ')
    # empregado1.setAumento(0.1)
    # print(empregado1.getSalario())  
    # print('\n=== Método set e get Nome: ')
    # empregado1.setNome('Murilo')
    # print(empregado1.getNome())
    # print('\n=== Método set e get Sobrenome: ')
    # empregado1.setSobrenome('Dantas')
    # print(empregado1.getSobrenome())
    # print('\n=== Método set e get Salario: ')
    # empregado1.setSalario(-200)
    # print(empregado1.getSalario())
    # print('\n=== Empregado 1 Modificado:')
    # print(empregado1)

    print('\n fim do programa')

main()
