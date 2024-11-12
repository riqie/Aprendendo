class Dog:
    tricks = [] # class variable shared by all instances

    def __init__(self, name):
        self.name = name # instance variable unique to each instance

    def addTrick(self, trick):
        self.tricks.append(trick)