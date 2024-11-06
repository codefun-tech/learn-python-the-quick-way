import csv
import sqlite3
import argparse


def init_db(args):
    with sqlite3.connect("employees.db") as conn:
        cur = conn.cursor()

        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS employees (
                name TEXT,
                age INTEGER,
                sex TEXT,
                department TEXT,
                salary REAL
            )
            """
        )

        with open("employees.csv", "r") as csv_file:
            csv_dict_reader = csv.DictReader(csv_file)
            for row in csv_dict_reader:
                cur.execute(
                    "INSERT INTO employees (name, age, sex, department, salary) VALUES (?, ?, ?, ?, ?)",
                    (
                        row["name"],
                        row["age"],
                        row["sex"],
                        row["department"],
                        row["salary"],
                    ),
                )

        conn.commit()


def clear_db(args):
    with sqlite3.connect("employees.db") as conn:
        cur = conn.cursor()

        cur.execute(f"DELETE FROM {args.table}")

        conn.commit()


def list_(args):
    with sqlite3.connect("employees.db") as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()

        cur.execute("SELECT * FROM employees")
        records = cur.fetchall()

        match args.item:
            case "employees":
                for record in records:
                    print(record["name"])
            case "departments":
                departments = []
                for record in records:
                    departments.append(record["department"])
                for department in set(departments):
                    print(department)


if __name__ == "__main__":
    # Set up the argument parser
    parser = argparse.ArgumentParser(
        description="Employee Management System", add_help=True
    )
    parser.add_argument("-v", "--version", action="version", version="%(prog)s 1.0.0")

    # Set up subparsers
    subparsers = parser.add_subparsers()

    db_parser = subparsers.add_parser("db", help="Database operations")
    db_subparsers = db_parser.add_subparsers()

    # Set up the init subparser without arguments
    parser_init = db_subparsers.add_parser("init", help="Initialize the database")
    parser_init.set_defaults(func=init_db)

    # Set up the clear subparser with arguments
    parser_clear = db_subparsers.add_parser("clear", help="Empty the table")
    parser_clear.add_argument("table", help="table name")
    parser_clear.set_defaults(func=clear_db)

    # Set up the list subparser with arguments
    parser_list = subparsers.add_parser(
        "list",
        description="list employees or departments",
        help="list employees or departments",
    )
    parser_list.add_argument(
        "-i",
        "--item",
        choices=("employees", "departments"),
        help="item to list",
    )
    parser_list.set_defaults(func=list_)

    # Parse arguments
    args = parser.parse_args()
    args.func(args)
