class Dog:

    def __init__(self, name):
        self.name = name # instance variable unique to each instance
        self.tricks = [] # class variable shared by all instances

    def addTrick(self, trick):
        self.tricks.append(trick)