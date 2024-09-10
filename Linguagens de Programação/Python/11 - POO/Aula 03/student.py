class Student:
    def __init__(self,name,roll,age,number):
        self.name = name
        self.roll = roll
        self.__age = age
        self.scores = []

        for count in range(number):
            self.scores.append(0)

    def __str__(self):
        return 'Name: ' + self.name +\
            '\nRoll: ' + self.roll +\
            '\nAge: ' + str(self.__age) +\
            '\nScores: ' + ' '.join(map(str, self.scores))
    
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name
    
    def getRoll(self):
        return self._roll

    def getAge(self):
        return self.__age
            
