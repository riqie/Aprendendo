from student import Student
nameStudent = input('Student name: ')
cpfStudent = input('CPF: ')
myStudent = Student(nameStudent, cpfStudent)
print('\n')
myStudent.toDrink('Guaraná')
print()
myStudent.toDrink('Beer')
