import sys


def main():

    try:
        # If not 1 command line argument
        if len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")

        python_file = sys.argv[1]

        # If file name does not end in `.py`
        if not sys.argv[1].endswith(".py"):
            sys.exit("Not a Python file")

        # Return number of lines of code in file
        print(count_lines(python_file))

    except FileNotFoundError:
        sys.exit("File does not exist")


# Count the lines of code
def count_lines(python_file):
    number_of_lines = 0

    try:
        # Open file in read mode
        with open(python_file, "r") as file:
            lines = file.readlines()

            for line in lines:
                # Strip whitespace from start of lines
                line = line.lstrip()
                # if line starts with `#` or only contains whitespace, do not count
                if line.startswith("#") or line.strip() == "":
                    continue
                # Update line count
                number_of_lines += 1

        return number_of_lines

    except FileNotFoundError:
        raise FileNotFoundError("File does not exist")


if __name__ == "__main__":
    main()
