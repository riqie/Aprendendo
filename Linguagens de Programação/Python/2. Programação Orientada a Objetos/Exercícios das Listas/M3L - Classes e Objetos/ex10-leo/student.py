"""10. Adicione três métodos à classe Student estudada em sala que compara dois objetos
Student. Um método deve testar a igualdade. Um segundo método deve testar para
menor que. O terceiro método deve testar para maior que ou igual a. Em cada caso, o
método retorna o resultado da comparação dos nomes dos dois alunos. Inclua uma
função main que testa todos os operadores de comparação. Em seguida, coloque
vários objetos Student em uma lista e embaralhe. Em seguida, execute o método sort
com esta lista e exiba todas as informações dos alunos."""

class Student:
     
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def __str__(self):
        return f"{self.name}: {self.grade}"
    
    def equals(self, other):
        if not isinstance(other, Student):
            return False
        return self.grade == other.grade
    
    def less_than(self, other):
        if not isinstance(other, Student):
            return False
        return self.grade < other.grade
    
    def greater_or_equal(self, other):
        if not isinstance(other, Student):
            return False
        return self.grade >= other.grade

