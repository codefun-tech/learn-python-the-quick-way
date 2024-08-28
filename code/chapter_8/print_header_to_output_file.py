output_file = open("output.csv", "w")

header = "name, age, sex, department, salary"
print(header, file=output_file)

output_file.close()
