import csv

with open("employees.csv", mode="r") as csv_read_file:
    with open("male_employees.csv", mode="w") as csv_write_file:
        header = ["name", "age", "sex", "department", "salary"]

        csv_read_file_reader = csv.DictReader(csv_read_file)
        csv_write_file_writer = csv.DictWriter(csv_write_file, fieldnames=header)

        csv_write_file_writer.writeheader()

        for record in csv_read_file_reader:
            if record["sex"] == "male":
                csv_write_file_writer.writerow(record)
