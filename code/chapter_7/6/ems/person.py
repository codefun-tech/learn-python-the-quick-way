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
