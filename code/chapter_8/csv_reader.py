import csv

with open("employees.csv", mode="r") as csv_file:
    csv_reader = csv.reader(csv_file)

    for record in csv_reader:
        print(record)
