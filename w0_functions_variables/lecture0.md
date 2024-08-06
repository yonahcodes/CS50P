# CS50P W0 - Functions & Variables
<br>

**Concatenation**
```python
print("hello, " + name)
```
<br>

**F-string**
```python
print(f"hello, {name}")
```
<br>

**Adds space automatically `sep=" "`**
```python
print("hello, ", name)
```
<br>

**Replace automatic new line `end="\n"`**
```python
print("hello, ", end="")
print(name)
```
<br>

**Print `""` inside of `" "`** 
```python
print('hello, "friend"') or print("hello, \"friend\"") 
```
<br>

**Remove `char` from string**
```python 
name = name.remove("c")
print(f"hello, {name}")
```
<br>

**Remove whitespace before and after word**
```python
name = name.strip()
print(f"hello, {name}")
```
<br>

**Remove prefix** 
```python
str.removeprefix("$")
```

**Remove suffix**
```python 
str.removesuffix("%")
```
<br>

**Replace one argument by another**
```python 
s = "hello world"
s = s.replace(" ", "...")
```
Output:
```	
`hello…world`
```
<br>

**Capitalize first letter of first word**
```python 
name = name.capitalize()
print(f"hello, {name}")
```
<br>

**Capitalize first letter of each word**
```python 
name = name.title()
print(f"hello, {name}")
```
<br>

**Combine several methods** 
```python
name = name.strip().title()
or
name = input("What's your name? ").strip().title()
```
<br>

**Split sentences**
```python	
first, last = name.split(" ")
print(f"hello, {first}")
```
<br>

**Python interactive mode >>>**
``` 
`python` to enter
`ctrl + d` to exit
```
<br>

**Convert user input to `int` or `float`** 
```python
x = int(input("What's x? "))
x = float(input("What's x? "))
```
<br>

**Round float to the nearest integer** 
```python
x = float(input("What's x? "))
y= float(input("What's y "))
z = round(x + y)
```
<br>

**Specify the number of digits to round to** 
```python
round(number[n, ndigits])
z = round(x / y, 2)
or
print(f"{z:.2f}")
```
<br>

**Format long numbers to include commas or points** 
```python
print(f"{z:,}")
```
<br>

**Define our own function** 
```python
def function_name():
	...
	...
def hello(to):
    print("hello,", to)
```
<br>

**Assign a default value to the parameter `to`** 
```python
def hello(to="world")
    print("hello,", to)

hello()
name = input("What’s your name? ")
hello(name)
```
<br>

**Define a `main()` function** 
```python	
def main():
	name = input("What's your name? ")
	hello(name)

def hello(to="world"):
	print("hello,", to)

main()
```
> Very important to *call* `main()` at the end of the file and to pass the variable between functions (scope)

<br>

**Define a function that returns square of `n`**
```python
def square(n):
	return n * n
	or
	return pow(n, 2) 	#(number, exponent)
```
<br>

**Define a function to raise to the power of 2** 
```python
def power(n):
	return n ** 2
```
<br>

**Split a camel case string (camelCaseString) into several substrings (`regex`)** 
```python
import re

def split_camel_case(s):
    return re.split("(?=[A-Z])", s)		
```
<br>

**Concatenate all elements of a list into a single string**
```python	
"<Separator>".join(list)
```
<br>

**Iterate through a string to find vowels**
```python 
def vowelless():
	vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
	for c in txt:
    	if c in vowels:
	    	…
```
<br>

**Irritate through each index `[i]` and character `c` in a string**
```python
for i, c in enumerate(string):
    …
```
