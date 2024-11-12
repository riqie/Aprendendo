class Person:
    @staticmethod
    def verifyName(name):
        return len(name) >= 3 and ' ' not in name
