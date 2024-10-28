# import the Employee class from the employee module in the ems package
from ems.employee import Employee

employee_john = Employee("John", 28, "Financial Department", salary=10000)
employee_jane = Employee("Jane", 26, "Human Resources Department", salary=8000)
print(employee_john + employee_jane)