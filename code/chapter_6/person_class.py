class Person:
    def __init__(self, name, age):
        self.name = name  # parameter name's value is assigned to the data attribute of the same name
        self.age = age  # parameter age's value is assigned to the data attribute of the same name

    # method update_age() is defined to update the data attribute self.age
    def update_age(self, age):
        self.age = age  # parameter age's value is assigned to the data attribute of the same name
