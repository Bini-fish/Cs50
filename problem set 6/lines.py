import sys


def main():
    line_counter()


def line_counter():
    # checking for appropriate number of arguments
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) == 2:
        pass

    path = sys.argv[1]  # initializing our input
    file_type = sys.argv[1].split(".")
    # checking if the argument is a python file
    if file_type[-1] != "py":
        sys.exit("Not a Python file")

    try:
        count = 0
        file = open(path, "r")
        for line in file.read().splitlines():
            if len(line.strip()) == 0:
                continue

            if not line.strip().startswith("#"):
                count += 1

    except FileNotFoundError:
        sys.exit("File does not exist")

    print(count)


if __name__ == "__main__":
    main()
