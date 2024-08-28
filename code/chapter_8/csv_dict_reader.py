import csv

with open("employees.csv", mode="r") as csv_file:
    csv_dict_reader = csv.DictReader(csv_file)

    for record in csv_dict_reader:
        print(record)
