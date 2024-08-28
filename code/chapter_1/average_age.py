import csv

# open the CSV file
with open("employees.csv", mode="r") as csv_file:
    # read the data in the CSV file
    csv_dict_reader = csv.DictReader(csv_file)

    num = 0
    sum_of_age = 0

    # iterate over each row of data
    for record in csv_dict_reader:
        # count the number of employees
        num += 1
        # sum up the age of employees
        sum_of_age += int(record["age"])

    # calculate the average age of employees
    average_age = sum_of_age / num

    # print the result
    print(f"Average age of employees: {average_age}")
