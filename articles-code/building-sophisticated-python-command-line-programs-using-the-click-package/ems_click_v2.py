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


@click.group(help="Employee Management System.")
def ems():
    pass


ems.add_command(init_db)
ems.add_command(clear_db)


if __name__ == "__main__":
    ems()
