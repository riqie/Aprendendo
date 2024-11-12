class Artist:
    def __init__(self, type):
        self.__type = type

    def present(self):
        print(f'The {self.__type} is performing his show!')
        