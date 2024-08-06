# CS50P W3 - Exceptions

## try and except

```py
x = int(input("What's x? "))
print(f"x is {x}")
```
>If user input is a `str`, we will get the runtime error `ValueError` (the value of variable is not the one expected).

<br>

1. 
```py
try:
    x = int(input("What's x? "))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")
```
<br>

2. Best practice is we should `try` the fewest lines of code possible
```py
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")

print(f"x is {x}")
```
> Now if user input is a str, we will get the runtime error NameError: name ‘x’ is not defined. This is because the wrong input triggers the Error handling `except` before ‘x’ gets to be defined.

<br>

3.  try and except with `else` block
```py
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")
```
> Now if the except block does not get triggered, the `else` block will.

<br>

4. try and except with `while` loop and `else` block
```py
while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break
print(f"x is {x}")
```
> Now, with the `while` loop, if the except block gets triggered, the program will prompt the user again infinitely until the right value is entered. 

<br>

5. Create the function `get_int()`
```py
def main():
    x = get_int()
        print(f"x is {x}")

# Version 1
def get_int():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not an integer")
        else:
            break
    return x

main()
```
```py
# Version 2
def get_int():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not an integer")
        else:
            return x
```
> The break is not needed, `return x` will stop the loop while returning the value.

<br>

```py
# Version 3
def get_int():
    while True:
        try:
            x = int(input("What's x? "))
	        return x
        except ValueError:
            print("x is not an integer")
```
> The `else` block can be removed. Placing `return x` in the `try` statement

<br>

```py
# Version 4
def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            print("x is not an integer")
```
> We can even avoid an extra line for the `return` x statement and avoid defining x explicitly by `returning` the result of `int(input(...))`

<br>

6. try and except with `pass` 
```py
def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            pass
```
> We can use the `pass` keyword to not act on the error and simply prompt again.

<br>

7. Final refined version of `get_int()` adding a function parameter 
```py
def main():
    x = get_int("What's x? ")
    print(f"x is {x}")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
	        pass

main()
```
> We can improve the implementation of the `get_int()` function. It is a good idea for `main()` to show the prompt argument `("What's x? ")` and the `get_int()` to accept a parameter (prompt).

<br>

## distances.py

```py
distances = {
    "Voyager 1": "163",
    "Voyager 2": "136",
    "Pioneer 10": "80 AU",
    "New Horizons": "58",
    "Pioneer 11": "44 AU"
}

def main():
    spacecraft = input("Enter a spacecraft: ")
    m = convert(distances[spacecraft])
    print(f"{m} m away")

def convert(au):
    return au * 149597870700

main()
```
> Because passing a `string` to the `convert()` function, the function will attempt to multiply the string by the huge number and this code will result in a `MemoryError`. We need to convert the string before converting the units.

<br>

1. 
```py
def main():
    spacecraft = input("Enter a spacecraft: ")
    au = float(distances[spacecraft])
    m = convert(au)
    print(f"{m} m away")
```
> Now we fixed the `string` problem converting the strings to `floats` before they are passed in as arguments to `convert()`. But we still have **messy data** in some of the key-value pairs, where the value is a string composed of **letters** and **digits** = `ValueError`

<br>

2. try and except
```py
def main():
    spacecraft = input("Enter a spacecraft: ")
    try:
        au = float(distances[spacecraft])
    except ValueError: 
	    print(f"Can’t convert '{distances[spacecraft]}' to a float")
        return

        m = convert(au)
    print(f"{m} m away")
```
> The `try` and `except` block will now handle the `ValueError`.

<br>

3. Adding except blocks for different **errors**
```py
def main():
    spacecraft = input("Enter a spacecraft: ")
    
    try:
        au = float(distances[spacecraft])
    except KeyError:
	    print(f" '{spacecraft}' is not in dictionary")
        return
    except ValueError: 
	    print(f"Can't convert '{distances[spacecraft]}' to a float")
        return

        m = convert(au)
    print(f"{m} m away")
```
> We now have an `except` block for each `ValueErrors` and `KeyErrors`. It is important to try to **anticipate potential errors** when writing code and include them in the try and except block.
