# open the employees file
employees_file = open("employees.csv")

# read the first line of the file, i.e., the header
line = employees_file.readline()
print("Header:")
print(line)

print("Employees Data:")
# iterate through and print the remaining lines, i.e., employee records
for line in employees_file:
    print(line)
# after the for loop, all lines have been printed
print("The End!")

# nothing is left to read from, so an empty string is returned
line = employees_file.readline()
if line == "":
    print("There is nothing to print!")

# when you are done with the file, you must close it
employees_file.close()
