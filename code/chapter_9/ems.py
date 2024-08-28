import csv
import argparse


def list_(args):
    with open("employees.csv", mode="r") as csv_file:
        csv_dict_reader = csv.DictReader(csv_file)

        match args.item:
            case "employees":
                for record in csv_dict_reader:
                    print(record["name"])
            case "departments":
                departments = []
                for record in csv_dict_reader:
                    departments.append(record["department"])
                for department in set(departments):
                    print(department)


def show(args):
    with open("employees.csv", mode="r") as csv_file:
        csv_dict_reader = csv.DictReader(csv_file)

        for record in csv_dict_reader:
            if record["name"] == args.name:
                print(f"name: {record['name']}")
                print(f"age: {record['age']}")
                print(f"sex: {record['sex']}")
                print(f"department: {record['department']}")
                print(f"salary: {record['salary']}")
                return

        print(f"There is no employee called {args.name} in this company.")


def employees_num():
    with open("employees.csv", mode="r") as csv_file:
        csv_dict_reader = csv.DictReader(csv_file)

        num = 0
        for record in csv_dict_reader:
            num += 1
        print(f"Number of employees: {num}")


def employees_average_age():
    with open("employees.csv", mode="r") as csv_file:
        csv_dict_reader = csv.DictReader(csv_file)

        num = 0
        sum_of_age = 0
        for record in csv_dict_reader:
            num += 1
            sum_of_age += int(record["age"])

        average_age = sum_of_age / num
        print(f"Average age of employees: {average_age}")


def departments_num():
    with open("employees.csv", mode="r") as csv_file:
        csv_dict_reader = csv.DictReader(csv_file)

        departments = []
        for record in csv_dict_reader:
            departments.append(record["department"])

        num_of_departments = len(set(departments))
        print(f"Number of departments: {num_of_departments}")


def describe(args):
    employees_num()
    employees_average_age()
    departments_num()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Employee Management System", add_help=True
    )
    parser.add_argument("--version", action="version", version="%(prog)s 6.0")

    subparsers = parser.add_subparsers(title="commands")

    # Setup the list parser
    parser_list = subparsers.add_parser(
        "list",
        description="list employees or departments",
        help="list employees or departments",
    )

    parser_list.add_argument(
        "item",
        choices=("employees", "departments"),
        help="item to list",
    )

    parser_list.set_defaults(func=list_)

    # Setup the show parser
    parser_show = subparsers.add_parser(
        "show",
        description="show employee infomations",
        help="show employee infomations",
    )

    parser_show.add_argument(
        "name",
        help="list employee information",
    )

    parser_show.set_defaults(func=show)

    # Setup the describe parser
    parser_describe = subparsers.add_parser(
        "describe",
        description="show company infomations",
        help="show company infomations",
    )

    parser_describe.set_defaults(func=describe)

    args = parser.parse_args()
    args.func(args)
