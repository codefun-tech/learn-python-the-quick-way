class Person:
    species = "Homo sapiens"

    def __init__(self, name, age):
        self._name = name
        self._age = age

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
    def __init__(self, name, age, department):
        Person.__init__(self, name, age)
        self._department = department

    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, department):
        self._department = department
