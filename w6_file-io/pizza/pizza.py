import csv
import sys
from tabulate import tabulate


def main():
    try:
        # Ensure correct number of command-line arguments (1)
        if len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")

        # Assign second c-l argument (csv file) to a variable
        csv_file = sys.argv[1]

        # Ensure file is a csv file
        if not csv_file.endswith(".csv"):
            sys.exit("Not a CSV file")

        # Print transformed file
        print(ascii_art(csv_file))

    # Handle file not found error
    except FileNotFoundError:
        sys.exit("File does not exist")


def ascii_art(csv_file):
    # Initialize empty list to store the DictReader result
    table = []

    try:
        # Open file in read mode
        with open(csv_file, "r") as file:
            # Create DictReader object to read file as dictionary
            reader = csv.DictReader(file)
            # Loop through rows in reader and append it to `table` list
            for row in reader:
                table.append(row)

        # Pass the `table` list, specify that headers are the keys,
        # and specify table forma to the tabualte function,
        # which will return ASCII table
        return tabulate(table, headers="keys", tablefmt="grid")

    except FileNotFoundError:
        raise FileNotFoundError("File does not exist")


if __name__ == "__main__":
    main()

