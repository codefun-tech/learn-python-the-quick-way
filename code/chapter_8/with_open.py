with open("employees.csv") as employees_file:
    line = employees_file.readline()
    print("Header:")
    print(line)

    print("Employees Data:")
    for line in employees_file:
        print(line)
    print("The End!")

    line = employees_file.readline()
    if line == "":
        print("There is nothing to print!")

print(employees_file.closed)
