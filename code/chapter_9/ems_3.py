import csv
import argparse


def list_(args):
    with open("employees.csv", mode="r") as csv_file:
        csv_dict_reader = csv.DictReader(csv_file)

        for record in csv_dict_reader:
            print(record["name"])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Employee Management System", add_help=True
    )
    parser.add_argument("--version", action="version", version="%(prog)s 3.0")

    subparsers = parser.add_subparsers(title="commands")

    # Setup the list parser
    parser_list = subparsers.add_parser(
        "list",
        description="list employees",
        help="list employees",
    )

    parser_list.add_argument(
        "item",
        choices=("employees",),
        help="item to list",
    )

    parser_list.set_defaults(func=list_)

    args = parser.parse_args()
    args.func(args)
