output_file = open("output.csv", "w")

header = "name, age, sex, department, salary"
output_file.write(header)

record = "Jone, 28, male, Financial, 10000"
output_file.write(record)

output_file.close()
