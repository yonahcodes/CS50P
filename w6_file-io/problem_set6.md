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
