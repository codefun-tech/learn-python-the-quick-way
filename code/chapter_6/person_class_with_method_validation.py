class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def update_name(self, name):
        print("You can't change the employee's name!")

    def update_age(self, age):
        if age < 18 or age > 60:
            print("Cannot hire employees younger than 18 or older than 60!")
            return
        self.age = age
