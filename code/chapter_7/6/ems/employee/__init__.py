# import the Person class from the person module in the parent folder of the employee package
from ..person import Person


class Employee(Person):
    def __init__(self, name, age, department, salary):
        Person.__init__(self, name, age)
        self._department = department
        self._salary = salary

    def __repr__(self):
        return f"<Employee: name={self.name}, age={self.age}, department={self.department}>"

    def __str__(self):
        return f"This is {self.name}, his/her age is {self.age}, he/she works in {self.department}."

    def __add__(self, other_employee):
        return self.salary + other_employee.salary

    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, department):
        self._department = department

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, department):
        self._salary = department
