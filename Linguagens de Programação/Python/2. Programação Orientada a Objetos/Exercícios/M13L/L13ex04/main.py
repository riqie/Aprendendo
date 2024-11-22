'''
4. Implemente um sistema de Empresa com os tipos de funcionários (gerente, vendedor,
recepcionista, secretário, etc.), evidenciando a classe Employee como uma classe
abstrata.
'''

from employee import *


def main():
    print("\nO programa fará:\n - cria uma empresa\n - cria seus funcionarios\n - evidencia a classe Emloyee como abstrata\n - classes dos funcionarios recebe o metodo da classe abstrata ")

    print("\nEmpresa: GreatTechnology")
    print("\nFuncionários:")

    employees = [
        Manager("Alice", 8000),
        Salesperson("Bob", 5000),
        Receptionist("Charlie", 3000),
        Secretary("Diana", 4000)
    ]

    for employee in employees:
        print(employee.get_details())
        print(employee.work())

    print()

main()