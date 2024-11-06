import csv
import sqlite3

import click


@click.command("init", help="Initialize the database.")
def init_db():
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


@click.command("clear", help="Empty the table.")
@click.argument("table", type=str, required=True)
def clear_db(table):
    with sqlite3.connect("employees.db") as conn:
        cur = conn.cursor()

        cur.execute(f"DELETE FROM {table}")

        conn.commit()


@click.command("list", help="List employees or departments.")
@click.option(
    "-i",
    "--item",
    type=click.Choice(["employees", "departments"], case_sensitive=False),
    required=True,
)
def list_(item):
    with sqlite3.connect("employees.db") as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()

        cur.execute("SELECT * FROM employees")
        records = cur.fetchall()

        match item:
            case "employees":
                for record in records:
                    print(record["name"])
            case "departments":
                departments = []
                for record in records:
                    departments.append(record["department"])
                for department in set(departments):
                    print(department)


@click.command("show", help="Show employee information.")
@click.argument("name", type=str, required=True)
def show(name):
    with sqlite3.connect("employees.db") as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()

        cur.execute("SELECT * FROM employees")
        records = cur.fetchall()

        for record in records:
            if record["name"] == name:
                print(f"name: {record['name']}")
                print(f"age: {record['age']}")
                print(f"sex: {record['sex']}")
                print(f"department: {record['department']}")
                print(f"salary: {record['salary']}")
                return

        print(f"There is no employee called {name} in this company.")


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


@click.command("describe", help="Describe the company.")
def describe():
    _employees_num()
    _employees_average_age()
    _departments_num()


@click.group(help="Employee Management System.")
def ems():
    pass


@click.group(help="Manage the database.")
def db():
    pass


ems.add_command(db)
ems.add_command(list_)
ems.add_command(show)
ems.add_command(describe)

db.add_command(init_db)
db.add_command(clear_db)


if __name__ == "__main__":
    ems()
