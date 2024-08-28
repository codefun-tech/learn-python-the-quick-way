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


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Employee Management System", add_help=True
    )
    parser.add_argument("--version", action="version", version="%(prog)s 5.0")

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

    args = parser.parse_args()
    args.func(args)
