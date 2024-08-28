import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Displays employees' informations.", add_help=True
    )

    parser.add_argument("--version", action="version", version="%(prog)s 2.0")

    parser.parse_args()
