import csv
import sys


def main():
    try:
        # Ensure correct number of command-line arguments (2)
        if len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")

        # Assign c-l arguments (csv files) to variables
        input_csv = sys.argv[1]
        output_csv = sys.argv[2]

        # Clean data from first csv file and return new csv
        clean_data(input_csv, output_csv)


    # Handle file not found error
    except FileNotFoundError:
        sys.exit(f"Could not read {input_csv}")


def clean_data(input_csv, output_csv):
    try:
        # Open input and output files
        with open(input_csv, "r") as input_file, open(output_csv, "w", newline='') as output_file:
            # Create DictReader object to read file as dictionary
            reader = csv.DictReader(input_file)
            # Create DictWriter object to write file as dictionary with specified fieldnames
            writer = csv.DictWriter(output_file, fieldnames=["first", "last", "house"])
            # Write fieldnames
            writer.writeheader()

            for row in reader:
                # Split csv file "name" key in two variables (using , as separator) and strip quotes
                last, first = row["name"].strip('"').split(",")
                # House key stays the same
                house = row["house"]
                # write row to new csv specifiying dictionary to be passed
                writer.writerow({"first": first.strip(), "last": last.strip(), "house":house})

    # Handle file not found error
    except FileNotFoundError:
        sys.exit(f"Could not read {input_csv}")


if __name__ == "__main__":
    main()

