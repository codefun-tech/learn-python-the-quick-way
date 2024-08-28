class Person:
    species = "Homo sapiens"

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def __repr__(self):
        return f"<Person: name={self.name}, age={self.age}>"

    def __str__(self):
        return f"This is {self.name}, his/her age is {self.age}."

    def __add__(self, other_person):
        return self.age + other_person.age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age < 18 or age > 60:
            print("Cannot hire employees younger than 18 or older than 60!")
            return
        self._age = age


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


# the code block of the if statement will be executed only when ems.py is run as a script
# and will not be executed when ems.py is imported as a module
if __name__ == "__main__":
    employee_john = Employee("John", 28, "Financial Department", salary=10000)
    employee_jane = Employee("Jane", 26, "Human Resources Department", salary=8000)
    print(employee_john + employee_jane)
    print(__name__)
