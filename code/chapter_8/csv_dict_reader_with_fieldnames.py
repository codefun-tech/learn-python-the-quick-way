import csv

with open("employees_records.csv", mode="r") as csv_file:
    csv_reader = csv.DictReader(
        csv_file, fieldnames=["name", "age", "sex", "department", "salary"]
    )

    for record in csv_reader:
        print(record)
