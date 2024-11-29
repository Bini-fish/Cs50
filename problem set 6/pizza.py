import sys
from tabulate import tabulate
import csv

def main():
    pizza()


def pizza():
    # checking for appropriate number of arguments
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) == 2:
        pass

    path = sys.argv[1]  # initializing our input
    file_type = path.split(".")
    # checking if the argument is a CSV file
    if file_type[-1] != "csv":
        sys.exit("Not a CSV file")
    try: 
        with open(path) as file:
            file = csv.reader(file, delimiter=',')
            table = tabulate(file, tablefmt="grid")
    except FileNotFoundError:
        sys.exit("File does not exist")

    print(table)


if __name__ == "__main__":
    main()
