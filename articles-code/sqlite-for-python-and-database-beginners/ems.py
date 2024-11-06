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


def show(args):
    with sqlite3.connect("employees.db") as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()

        cur.execute("SELECT * FROM employees")
        records = cur.fetchall()

        for record in records:
            if record["name"] == args.name:
                print(f"name: {record['name']}")
                print(f"age: {record['age']}")
                print(f"sex: {record['sex']}")
                print(f"department: {record['department']}")
                print(f"salary: {record['salary']}")
                return

        print(f"There is no employee called {args.name} in this company.")


def _employees_num():
    with sqlite3.connect("employees.db") as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()

        cur.execute("SELECT * FROM employees")
        records = cur.fetchall()

        num = 0
        for _ in records:
            num += 1
        print(f"Number of employees: {num}")


def _employees_average_age():
    with sqlite3.connect("employees.db") as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()

        cur.execute("SELECT * FROM employees")
        records = cur.fetchall()

        num = 0
        sum_of_age = 0
        for record in records:
            num += 1
            sum_of_age += int(record["age"])

        average_age = sum_of_age / num
        print(f"Average age of employees: {average_age}")


def _departments_num():
    with sqlite3.connect("employees.db") as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()

        cur.execute("SELECT * FROM employees")
        records = cur.fetchall()

        departments = []
        for record in records:
            departments.append(record["department"])

        num_of_departments = len(set(departments))
        print(f"Number of departments: {num_of_departments}")


def describe(args):
    _employees_num()
    _employees_average_age()
    _departments_num()


if __name__ == "__main__":
    # Set up the argument parser
    parser = argparse.ArgumentParser(
        description="Employee Management System", add_help=True
    )
    parser.add_argument("--version", action="version", version="%(prog)s 6.0")

    # Set up subparsers
    subparsers = parser.add_subparsers()

    # Set up the init subparser without arguments
    parser_init = subparsers.add_parser("init", help="Initialize the database")
    parser_init.set_defaults(func=init_db)

    # Set up the clear subparser with arguments
    parser_clear = subparsers.add_parser("clear", help="Empty the table")
    parser_clear.add_argument("table", help="table name")
    parser_clear.set_defaults(func=clear_db)

    # Set up the list subparser with arguments
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

    # Set up the show subparser with arguments
    parser_show = subparsers.add_parser(
        "show",
        description="show employee information",
        help="show employee information",
    )
    parser_show.add_argument(
        "name",
        help="list employee information",
    )
    parser_show.set_defaults(func=show)

    # Set up the describe subparser without arguments
    parser_describe = subparsers.add_parser(
        "describe",
        description="show company infomations",
        help="show company infomations",
    )
    parser_describe.set_defaults(func=describe)

    # Parse arguments
    args = parser.parse_args()
    args.func(args)
