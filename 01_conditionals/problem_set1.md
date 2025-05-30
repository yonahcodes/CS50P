# CS50P - Problem Set 1

## Deep Thought
Implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, outputting `Yes` if the user inputs `42` or (case insensitively) `forty-two` or `forty two`. Otherwise `No`.
```py
.lower()
```
```py
.strip()
```
<br>

## Home federal Savings Bank
Implement a program that prompts the user for a greeting. If the greeting starts with `"hello"`, output `0$`. If the greeting starts with an `"h"` (but not hello), output `20$`. Otherwise output `100$`.

- Ignore leading whitespace
- case-insensitive

```py
.strip()
```
```py
.lower()
```
```py
startswith()
```
<br>

## File Extensions
Implement a program that prompts the user for the name of a files and then outputs that file’s **media type** if the file’s name ends, case-insensitively, in any of these suffixes:
```
.gif = image/gif  
.jpg = image/jpg
.jpeg = image/jpeg
.png = image/png
.pdf = application/pdf
.txt = text/plain
.zip = application/zip
```
If the file name ends with some other suffix at all, output `application/octet-stream` instead.
```py
partition(".") # Splits string at first dot . 
```
```py
rpartition(".") # Splits string at last dot .
```
```py
media = f"image/{suffix}"
```
<br>

## Math Interpreter
Implement a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a `floating-point value` formatted to one decimal place. 

Assume that the user’s input will be formatted as `x y z` with one space between `x` and `y` and one space between y and z:
```
X is an integer
Y is +,-,*, or /
Z is an integer
```
```py
.split(" ")
```
```py
return f"{result:.1f}"
```
<br>

## Meal Time
Implement a program that prompts the user for a time and outputs whether it's breakfast time, lunch time, or dinner time.

- If it's not time for a meal, don't output anything at all.

- User input formatted in 24-hour time as `#:##` or `##:##`.

- `convert(time)` : converts 07:30 string into 7.5 float

- Each meal's time range in inclusive : 
```
7:00 - 8:00 Breakfast
12:00 - 13:00 Lunch
18:00 - 19:00 Dinner
```
<br>

> `__name__` has two "`_`"
