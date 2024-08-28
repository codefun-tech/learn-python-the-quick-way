import csv

with open("dict_writer_employees.csv", mode="w") as csv_file:
    header = ["name", "age", "sex", "department", "salary"]
    csv_dict_writer = csv.DictWriter(csv_file, fieldnames=header)
    csv_dict_writer.writeheader()

    record = {
        "name": "Nina",
        "age": "24",
        "sex": "female",
        "department": "Financial",
        "salary": "80000",
    }
    csv_dict_writer.writerow(record)
