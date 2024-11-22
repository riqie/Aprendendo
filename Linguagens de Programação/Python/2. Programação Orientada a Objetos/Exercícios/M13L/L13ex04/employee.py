from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    @abstractmethod
    def work(self):
        pass

    def get_details(self):
        return f"\nName: {self.__name}, Salary: {self.__salary}"
    
    def getName(self):
        return self.__name


class Manager(Employee):
    def work(self):
        return f"{self.getName()} is managing the team."


class Salesperson(Employee):
    def work(self):
        return f"{self.getName()} is selling products."


class Receptionist(Employee):
    def work(self):
        return f"{self.getName()} is answering calls."


class Secretary(Employee):
    def work(self):
        return f"{self.getName()} is organizing schedules."


