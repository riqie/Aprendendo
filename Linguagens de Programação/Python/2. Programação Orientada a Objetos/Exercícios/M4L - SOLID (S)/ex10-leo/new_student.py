"""10. Adicione três métodos à classe Student estudada em sala que compara dois objetos
Student. Um método deve testar a igualdade. Um segundo método deve testar para
menor que. O terceiro método deve testar para maior que ou igual a. Em cada caso, o
método retorna o resultado da comparação dos nomes dos dois alunos. Inclua uma
função main que testa todos os operadores de comparação. Em seguida, coloque
vários objetos Student em uma lista e embaralhe. Em seguida, execute o método sort
com esta lista e exiba todas as informações dos alunos."""

class Student:
     
    def __init__(self, name, grade):
        
        self.__name = self.verify_name(name)
        self.__grade = self.verify_grade(grade)
        
    
    def __str__(self):
        return f"{self.__name}: {self.__grade}"
    
    def equals(self, other):
        if self.verify_student(other):
            return self.__grade == other.__grade
        return self.indicateError()
    
    def less_than(self, other):
        if self.verify_student(other):
            return self.__grade < other.__grade
        return self.indicateError()
    
    def greater_or_equal(self, other):
        if self.verify_student(other):
            return self.__grade > other.__grade
        return self.indicateError()

    def verify_student(self,other):
        if not isinstance(other, Student):
            
            return 0
        return other.__grade
    
    
          
    def getGrade(self):
        return self.__grade
         
    def verify_name(self,name):
        if isinstance(name,str):
            return name
        return "Irregular name"
    
    def verify_grade(self,grade):
        if isinstance(grade,(int,float)):
            return grade
        return 0
