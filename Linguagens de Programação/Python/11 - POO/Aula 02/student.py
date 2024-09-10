'''
File: Student.py Features for managing a student's name and grades
'''

'''Represent a student'''
class Student:

    '''All scores are initially 0.'''
    def __init__(self, name, number):

        self.name = name
        self.scores = []
        
        for count in range(number):
            self.scores.append(0)

    '''Returns the string representation of the student''' 
    def __str__(self):

        return 'Name: ' + self.name + '\nScores: ' + \
            ' '.join(map(str, self.scores))


    '''Returns the student's name.'''
    def getName(self):

        return self.name
