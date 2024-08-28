with open("output.csv", "w") as output_file:
    header = "name, age, sex, department, salary\n"
    output_file.write(header)

    record = "John, 28, male, Financial, 10000\n"
    output_file.write(record)
