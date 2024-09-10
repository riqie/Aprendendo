from student import Student
nameStudent = input('Student name: ')
rollStudent = input('Roll: ')
ageStudent = input('Age: ')
qttGrades = int(input('Number of Grades: '))
myStudent = Student(nameStudent, rollStudent, ageStudent, qttGrades)

print(myStudent.getName())
nameStudent = input('New name: ')
myStudent.setName(nameStudent)
print(myStudent.getName())
