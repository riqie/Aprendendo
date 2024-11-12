"""10. Adicione três métodos à classe Student estudada em sala que compara dois objetos
Student. Um método deve testar a igualdade. Um segundo método deve testar para
menor que. O terceiro método deve testar para maior que ou igual a. Em cada caso, o
método retorna o resultado da comparação dos nomes dos dois alunos. Inclua uma
função main que testa todos os operadores de comparação. Em seguida, coloque
vários objetos Student em uma lista e embaralhe. Em seguida, execute o método sort
com esta lista e exiba todas as informações dos alunos."""

from student import Student
import random

def main():
    # Criar alguns objetos Student com notas
    students = [
        Student("Alice", 85),
        Student("Bob", 92),
        Student("Charlie", 78),
        Student("Diana", 90),
        Student("Eva", 88)
    ]
    
    # Testar os métodos de comparação
    student1 = students[0]  # Alice
    student2 = students[1]  # Bob
    
    print(f"Comparing: {student1} e {student2}:")
    print(f"Equals: {student1.equals(student2)}")
    print(f"Less Than: {student1.less_than(student2)}")
    print(f"Greater or Equal: {student1.greater_or_equal(student2)}")

    # Embaralhar a lista de estudantes
    random.shuffle(students)
    
    # Ordenar a lista de estudantes (por nota)
    students.sort(key=lambda s: s.grade)
    
    # Exibir informações dos alunos ordenados
    print("\nLista de alunos ordenada:")
    for student in students:
        print(student)
        
main()       

