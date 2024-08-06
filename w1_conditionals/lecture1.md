# CS50P W1 - Conditionals

## `if` Statements
```python
if x < y: 
    …
elif x > y:
    …
else : 
    …
```
```python
if x < y or x > y:
	…
else:
    …
```
```python
if x != y:
    …
else:
    …
```
```python
if score >= 90 and score <= 100:
	…
if 90 <= score <= 100:
    …
if score >= 90:
    …
```

## Modulo Operator `%`
Remainder of dividing two numbers not evenly
```
4 % 2 = 0 (divides evenly)
3 % 2 = 1 (dividing 3/2 = 1.5, the quotient is 1 and the remainder 0.5 x 2 = 1)
16 % 5 = 1 (dividing 16/5 = 3.2, the quotient is 3 and the remainder 0.2 x 5 = 1)
```
```python
if x % 2 == 0:
	print("Even")
else:
    print("Odd")
```

### `bool`
```python
def is_even(n):
    if n % 2 == 0:
 		return True
	else:
      	return False
```

**Pythonic syntax**
```python 
def is_even(n):
    return True if n % 2 == 0 else False

def is_even(n):
    return n % 2 == 0		# The operation automatically returns a bool

# Integrating `is_even()`
if is_even(x):
	print("Even")
```
<br>

## `match` Statements
<br>

1. 
```python
name = input("What’s your name? ")

if name == "Harry": 
	print("Gryffindor")
elif name == "Harry": 
	print("Gryffindor")
elif name == "Harry": 
	print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else : 
	print("Who?")
```
<br>

2. 
```python
name = input("What's your name? ")

if name == "Harry" or "Hermione" or "Draco": 
	print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else : 
	print("Who?")
```
<br>

3.  `match`
```python
name = input("What’s your name? ")

match name:
case "Harry": 
	print("Gryffindor")
 case “Hermione”: 
	print("Gryffindor")
case “Ron”: 
	print("Gryffindor")
case “Draco”:
    print("Slytherin")
case _:
    print("Who?")
```
<br>

4.
```python
match name:
    case "Harry" | "Hermione" | "Ron":
		print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
```
<br>

## Error Checking
```python
def main():
	difficulty = ("Enter level: ")
	if not (difficulty == "Difficult" or difficulty == "Casual"):
		print("Enter a valid difficulty")
		return
```
<br>

1. 
```python
if difficulty == "Difficult":
	if players == "Multiplayer":
		recommend("Poker")
```
<br>

2. 
```python
if difficulty == "Difficult" and players == "Multiplayer":
	recommend("Poker")
```
