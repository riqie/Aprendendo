from new_student import Student
import random
def main():
    # Criar alguns objetos Student com notas
    students = [
        Student(234, "leoo"),
        Student("Leonardo", 92),
        Student("Bob Chalton", 78),
        Student("Rafael", 90),
        Student("Murilo", 88)
    ]
    
    # Testar os métodos de comparação
    student1 = students[0]  
    student2 = students[1]  
    
    print(f"Comparando {student1} e {student2}:")
    print(f"Equals: {student1.equals(student2)}")
    print(f"Less Than: {student1.less_than(student2)}")
    print(f"Greater: {student1.greater_or_equal(student2)}")
    
    random.shuffle(students)
    
    # Ordenar a lista de estudantes (por nota)
    students.sort(key=lambda s: s.getGrade())
    
    # Exibir informações dos alunos ordenados
    print("\nLista de alunos ordenada:")
    for student in students:
        print(student)
main()       
