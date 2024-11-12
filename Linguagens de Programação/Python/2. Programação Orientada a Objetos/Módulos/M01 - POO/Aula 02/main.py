from student import Student
nameStudent = input('Student name: ')
qttGrades = int(input('Number of grades: '))

myStudent = Student(nameStudent, qttGrades)
print(myStudent.__str__())
