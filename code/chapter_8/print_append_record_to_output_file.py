output_file = open("output.csv", "a")

record = "Jone, 28, male, Financial, 10000"
print(record, file=output_file)

output_file.close()
