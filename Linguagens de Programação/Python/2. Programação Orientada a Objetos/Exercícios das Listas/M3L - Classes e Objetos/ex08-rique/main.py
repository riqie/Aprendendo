'''
Crie uma classe chamada Employee que inclui três variáveis de instância: um nome
(string), um sobrenome (string) e um salário mensal (float). Sua classe deve ter um
construtor que inicializa as três variáveis. Forneça um método get e set para cada
variável. Se o salário mensal fornecido pelo usuário não for positivo, configure-o
como 0.0. Teste a classe implementada e seus métodos. Crie dois objetos Employee e
exiba o salário anual de cada objeto. Depois, dê 10% de aumento para cada
empregado e exiba novamente os salários.
'''

from employee import Employee

def main():
    print('\nO programa fará o registro de 2 funcionários, depois a mudança de 1 deles.\n')
    funcionario1 = Employee('Henrique ', 'Carvalho ', 1000)
    funcionario2 = Employee('Rafael ','Leo ', 2500)

    print(f'Func1: {funcionario1.mostrar_funcionario()}\n\nFunc2: {funcionario2.mostrar_funcionario()}')
    print(f'\nSalários Anuais:\nFunc1: {funcionario1.getSalarioAnual()}\nFunc2: {funcionario2.getSalarioAnual()} ')

    print('\nFuncionamento dos métodos da classe para o funcionário 1: ')

    print('Funcionamento do método Aumento: ')
    funcionario1.setAumento(0.1)
    print(funcionario1.getSalario())  

    print('\nMétodo set e get Nome: ')
    funcionario1.setNome('Murilo')
    print(funcionario1.getNome())

    print('\nMétodo set e get Sobrenome: ')
    funcionario1.setSobrenome('Dantas')
    print(funcionario1.getSobrenome())

    print('\nMétodo set e get Salario: ')
    funcionario1.setSalario(20000)
    print(funcionario1.getSalario())

    print('\nFuncionario 1 Modificado:')
    print(funcionario1.mostrar_funcionario())

    print('\n fim do programa')

main()
