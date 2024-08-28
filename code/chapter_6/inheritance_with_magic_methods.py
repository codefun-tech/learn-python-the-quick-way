class Person:
    species = "Homo sapiens"

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def __repr__(self):
        return f"<Person: name={self.name}, age={self.age}>"

    def __str__(self):
        return f"Hello, my name is {self.name}, I'm {self.age} years old."

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

    def __repr__(self):
        return f"<Employee: name={self.name}, age={self.age}, department={self.department}>"

    def __str__(self):
        return f"Hello, my name is {self.name}, I'm {self.age} years old. I work in {self.department}."

    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, department):
        self._department = department
