class Student:
    def __init__(self,name,cpf):
        self.name = name
        self.__cpf = cpf


    def __str__(self):
        return 'Name: ' + self.name +\
            '\nRoll: ' + self.roll +\
            '\nAge: ' + str(self.__age) +\
            '\nScores: ' + ' '.join(map(str, self.scores))
    
    def __present_doct(self):
        print(self.__cpf)
    
    def toDrink(self, drink):
        if drink == 'Beer':
            self.__present_doct()
            print('Driking ' + drink)
