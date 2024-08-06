# CS50P W0 - Functions & Variables
<br>

**Concatenation**
```py
print("hello, " + name)
```
<br>

**F-string**
```py
print(f"hello, {name}")
```
<br>

**Adds space automatically `sep=" "`**
```py
print("hello, ", name)
```
<br>

**Replace automatic new line `end="\n"`**
```py
print("hello, ", end="")
print(name)
```
<br>

**Print `""` inside of `" "`** 
```py
print('hello, "friend"') or print("hello, \"friend\"") 
```
<br>

**Remove `char` from string**
```py 
name = name.remove("c")
print(f"hello, {name}")
```
<br>

**Remove whitespace before and after word**
```py
name = name.strip()
print(f"hello, {name}")
```
<br>

**Remove prefix** 
```py
str.removeprefix("$")
```

**Remove suffix**
```py 
str.removesuffix("%")
```
<br>

**Replace one argument by another**
```py 
s = "hello world"
s = s.replace(" ", "...")
```
Output:
```	
`hello…world`
```
<br>

**Capitalize first letter of first word**
```py 
name = name.capitalize()
print(f"hello, {name}")
```
<br>

**Capitalize first letter of each word**
```py 
name = name.title()
print(f"hello, {name}")
```
<br>

**Combine several methods** 
```py
name = name.strip().title()
or
name = input("What's your name? ").strip().title()
```
<br>

**Split sentences**
```py	
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
```py
x = int(input("What's x? "))
x = float(input("What's x? "))
```
<br>

**Round float to the nearest integer** 
```py
x = float(input("What's x? "))
y= float(input("What's y "))
z = round(x + y)
```
<br>

**Specify the number of digits to round to** 
```py
round(number[n, ndigits])
z = round(x / y, 2)
or
print(f"{z:.2f}")
```
<br>

**Format long numbers to include commas or points** 
```py
print(f"{z:,}")
```
<br>

**Define our own function** 
```py
def function_name():
	...
	...
def hello(to):
    print("hello,", to)
```
<br>

**Assign a default value to the parameter `to`** 
```py
def hello(to="world")
    print("hello,", to)

hello()
name = input("What’s your name? ")
hello(name)
```
<br>

**Define a `main()` function** 
```py	
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
```py
def square(n):
	return n * n
	or
	return pow(n, 2) 	#(number, exponent)
```
<br>

**Define a function to raise to the power of 2** 
```py
def power(n):
	return n ** 2
```
<br>

**Split a camel case string (camelCaseString) into several substrings (`regex`)** 
```py
import re

def split_camel_case(s):
    return re.split("(?=[A-Z])", s)		
```
<br>

**Concatenate all elements of a list into a single string**
```py
"<Separator>".join(list)
```
<br>

**Iterate through a string to find vowels**
```py
def vowelless():
	vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
	for c in txt:
    	if c in vowels:
	    	…
```
<br>

**Irritate through each index `[i]` and character `c` in a string**
```py
for i, c in enumerate(string):
    …
```
