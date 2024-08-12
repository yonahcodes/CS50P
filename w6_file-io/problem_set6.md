# CS50P Problem Set 6

## Lines of Code
In a file called `lines.py` implement a program that expects exactly one command-line argument, the **name** (or path) of a Python file, and outputs the **number of lines of code** in that file.
- Excluding **comments** and **blank lines**
- If user does not specify exactly **one** command-line argument, or if the specified file's name does not end in `.py`, the program should instead exit via `sys.exit`

Assume that any line that starts with `#`, optionally preceded by **whitespace**, is a comment.
- A `docstring` should not be considered a comment.

Assume that any line that only contains whitespace is blank.
<br>

```
# Expect one command line argument
    # If not 1 command line argument
        sys.exit("Two few command-line arguments")
    # If file name does not end in `.py`
        sys.exit("Not a Python file")
    # If file does not exist
        raise FileNotFoundError("File does not exist")
```
```
# Count the lines of code
    # Open File
        # If file does not exist
            raise FileNotFoundError("File does not exist")
        # Strip whitespace from start of lines
        # if line starts with #, do not count
        # if a line only contains whitespace = blank
```
```py
import sys
```
```py
lstrip()
```
```py
startswith()
```
```py
open()
```
```py
readlines()
```
```py
raise FileNotFoundError
```
<br>

## Pizza Py
Implement a program that expext one command-line argument, the name (or path) of a **CSV** file in Pinocchio's format, and outputs a table formatted as **ASCII** art using `tabulate`, a package on PyPI at pypi.org/project/tabulate.

- Format the tables using the library's `grid`format. 

- If the user does not specify exactly one command-line argument, or if the specified file's name does not end in `.csv`, of if the specified files does not exist:
    - The program should instead exit via `sys.exit`.

<br>

```py
import csv
import sys
from tabulate import tabulate
```
```py
tabulate(table, headers="keys", tablefmt="grid")
```
```py
reader = csv.DictReader(file)
for row in reader:
    table.append(row)
```
```py
except FileNotFoundError:
    raise FileNotFoundError("File does not exist")
```
<br>

## Scourgify
Implement a program that expects the user to provide two comand-line arguments:
- The name of an existing CSV file to read as input, whose columns are assumed to be, in order, `name` and `house`, and
- The name of a new CSV to write as output, whose columns should be, in order, `first`, `last`, and `house`.

If the user does not provide exactly two command-line arguments, or if the first cannot be read, the program should exit via `sys.exit`with an error message.

<br>

<br>

```py
import csv
import sys
```
```py
clean_data(input_csv, output_csv)
```
```py
with open(input_csv, "r") as input_file, open(output_csv, "w", newline='') as output_file:
```
```py
for row in reader:
last, first = row["name"].strip('"').split(",")
house = row["house"]
writer.writerow({"first": first.strip(), "last": last.strip(), "house":house})
```
```py
except FileNotFoundError:
    sys.exit(f"Could not read file {input_csv}")
```
<br>

