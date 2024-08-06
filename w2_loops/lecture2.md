# CS50P W2 - Loops

## While Loops
While the condition is true the loop keeps iterating. The only way to break the loop is for the condition to return false. If the condition stays true, the loop will be infinite:
```py
i = 3
while i != 0:
    print("meow")
```
> Use `cmd + c` to break out of a infinite loop

<br>

1. 
```py
i = 3
while i != 0:
    print("meow")
    i = i - 1
```
<br>

2. 
```py
i = 1
while i <= 3:
    print("meow")
    i = i + 1
```
<br>

3. 
```py
i = 0
while i < 3:
    print("meow")
    i += 1		# i += 1 == i = i + 1
```
<br>

### water.py
1. 
```py
from soil import sample

def main():
    moisture = sample()
    print(f"Moisture is {moisture}%")

    while moisture > 20:
        moisture = sample()
        print(f"Moisture is {moisture}%")

    print("Time to water!")

main()
```
> While moisture is more than 20% (condition is True), keep sampling the soil. When the condition becomes False (moisture less or equal to 20%), break the loop and print “Time to water!”.

<br>

2. 
```py
def main():
    moisture = sample()
    days = 0
    print(f"Moisture is {moisture}%")

    while moisture > 20:
        moisture = sample()
        days += 1
        print(f"Day {days}: Moisture is {moisture}%")

    print("Time to water!")
```
> While moisture is more than 20% (condition is True), keep sampling the soil and increase the day count by 1.

<br>

## For Loops
A `for` loop iterates through a list of items. Python automatically initializes (to `0`) and updates `i`  

1. 
```py
for i in [0, 1, 2]:
    print("meow")
```
<br>

2. 
```py
for i in range(3):
    print("meow")
```
> The `range()` built-in function takes one argument (the number of values you want back), starting at `0` up to (but not through) the specified value.

<br>

3. 
```py 
for _ in range(3):
    print("meow")
```
> The `"Pythonic"` way is to represent `i` with an underscore `_`

<br>

4. 
```py
print("meow" * 3)
```
> This code will output `meowmeowmeow`

<br>

5. 
```py
print("meow\n" * 3 end="")
```
> Adding a `\n` after the string and removing the automatic one after the print will output : 
```
meow
meow
meow
```
<br>

### User Input
1. 
```py
while True:
    n = int(input("What's n? "))
    if n < 0:
        continue
    else:
	    break
```
> If the user enters a negative (`< 0`) number the loop keeps asking for input until **entering a positive number breaks the loop**.

<br>

2. 
```py
while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")
```
<br>

3. 
```py
def main():
    meow(3)

def meow(n):
    for _ in range(n):
        print("meow")

main()
```
<br>

4. 
```py
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("meow")

main()
```
<br>

## Lists

```py
students = ["Hermione", "Harry", "Ron"]
```
<br>

1. 
```py
print(students[0])
print(students[1])
print(students[2])
```
2. 
```py
for student in students:
    	    print(student)
```
3. 
```py
for i in range(len(students)):
    print(students[i])
```
4. 
```py
for i in range(len(students)):
    print(i + 1, students[i])
```
```
1 Hermione
2  Harry
3 Ron
```
<br>

### Append elements to a list

1. 
```py
results = ["Mario", "Luigi"]

results.append("Princess")
results.append("Yoshi")
results.append("Koopa Troopa")
results.append("Toad")

print(results)
```
<br>

2. Append multiple elements at a time 
```py
results.append(["Bowser", "Donkey Kong Jr."])
```
> This will result in a separate sublist within the original list. The `extend()` method is better suited to append multiple elements to the list
```py
results.remove(["Bowser", "Donkey Kong Jr."])
results.extend(["Bowser", "Donkey Kong Jr."])
```
<br>

### Remove elements from a list
```py
results = ["Mario", "Luigi", "Princess", "Yoshi", "Koopa Troopa",
    "Toad", "Bowser", "Donkey Kong Jr."
]

results.remove("Bowser")
```
<br>

### Insert elements into a list in a specific index `insert(index, element)`
```py
results = ["Mario", "Luigi", "Princess", "Yoshi", "Koopa Troopa",
    "Toad", "Donkey Kong Jr."
]

results.insert(0,"Bowser")
```
<br>

### Reverse order of the elements of a list
```py
results = ["Mario", "Luigi", "Princess", "Yoshi", "Koopa Troopa",
    "Toad", “Bowser”, "Donkey Kong Jr."
]

results.reverse()
```
Output:
```py
["Donkey Kong Jr.", “Bowser”,"Toad", "Koopa Troopa",
"Yoshi", "Princess", "Luigi", "Mario"
]
```
<br>

## Dictionaries
Data structure that allows us to associate **keys** with **values**.

```py
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"}

print(students["Hermione"])
```
> We use the **key** as an index to retrieve the **value** associated with it.

<br>

1. 
```py
for student in students:
    print(student)
```
Printing the iterator `student` will print the **keys** in the list:  
```
Hermione
Harry
Ron
Draco
```
<br>

2. 
```py
for student in students:
    print(student, students[student])
```
Prints the keys `student`, and the values `students[student]`:
```
Hermione Gryffindor,
Harry Gryffindor
Ron Gryffindor
Draco Slytherin
```
<br>

3. 
```py
for student in students:
    print(student, students[student], sep=",")
```
Prints the keys `student`, and the values `students[student]`:
```
Hermione, Gryffindor
Harry, Gryffindor
Ron, Gryffindor
Draco, Slytherin
```

### report.py
```py
def main():
    spacecraft = {"name": "Voyager 1", "distance": 163}
    print(create_report(spacecraft))

def create_report(spacecraft):
    return f"""
    ========= REPORT =========

    Name: {spacecraft["name"]}
    Distance: {spacecraft["distance"]} AU

    ==========================
    """
```
> Notice the capabilities of the `f-strings`

<br>

#### Adding Keys

1. 
```py
spacecraft = {"name": "Voyager 1", "distance": 163}

spacecraft["distance"] = 0.01 
```
> We can add a key-value pair to a dictionary by indexing into the key and assigning a new value.

<br>

2. 
```py
spacecraft = {"name": "james Webb Space Telescope"}

spacecraft.update({“distance”: 0.01, “orbit”: “Sun”}) 
```
<br>

#### Error Checking 
```py
def create_report(spacecraft):
    return f"""
    ========= REPORT =========

    Name: {spacecraft.get("name", "Unknown")}
    Distance: {spacecraft.get("distance", "Unknown")} AU
    Orbit:  {spacecraft.get("orbit", "Unknown")}

    ==========================
    """
```
> `get(key, default_value)`: `spacecraft.get("distance", "Unknown")` will try to access the value associated with the `"distance"` key, if no value is found, it will default to returning `"Unknown"`

<br>

### distances.py

```py
distances = {
    "Voyager 1": 163,
    "Voyager 2": 136,
    "Pioneer 10": 80,
    "New Horizons": 58,
    "Pioneer 11": 44
}
```
<br>

#### Accessing keys
```py
def main():
    for name in distances.keys():
        print(f"{name} is {distances[name]} AU from Earth")
```
>If the keys in the dictionary are different, we can use the `keys()` method to access each of those keys. Notice the use of an **f-string** and the `distances[name]` 

<br>

#### Accessing values
```py
def main():
    for name in distances.values():
        print(f"{name} is {distances[name]} AU from Earth")
```
<br>

#### Converting values (AU to meters)
```py
def main():
    for distance in distances.values():
        print(f"{distance} AU is {convert(distance)} AU from Earth")

def convert(au):
    return au * 149597870700
```
<br>

## Lists of Dictionaries
```py
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]
```
> The keyword `None` means there is no value associated with the `"patronus"` key in the last dictionary.

<br>

1. 
```py
for student in students:
    print(student["name"])
```
> The iterator `student` now represents the dictionaries in the list. It prints the values associated with `"name"` key in each dictionary

<br>

2. 
```py
for student in students:
    print(student["name"], student["house"], student["patronus"], sep=",")
```
Prints the values associated with the `"name"`, `"house"`, and `"patronus"` keys (separated by a comma) in each dictionary:
```
Hermione, Gryffindor, Otter
Harry, Gryffindor, Stag
Ron, Gryffindor, Jack Russell terrier
Draco, Slytherin, None
```
<br>

## mario.py
1. 
```py
def print_column(height):
    for _ in range(height):
        print("#")
```
<br>

2. 
```py
def print_column(height):
    print("#\n" * height, end="")
```
<br>

3. 
```py
def print_row(width):
    print("?" * width)
```
<br>

## Nested loops
1. 
```py
def print_square(size):
    for i in range(size):
	    for j in range(size):
        	print("#")
	    print()
```
```py
def print_square(size):
	# For each row in square
    for i in range(size):
	    # For each brick in row
	    for j in range(size):
		    # Print brick
        	print("#")
	# Add new line at the end of the row
	print()
```
<br>

2. 
```py
def print_square(size):
    for i in range(size):
    	print("#" * size)
```
<br>

3. 
```py
def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)
```

## Letters.py

1. 
```py
def main():
    print(write_letter("Mario", "Princess Peach"))
    print(write_letter("Luigi", "Princess Peach"))
    print(write_letter("Daisy", "Princess Peach"))
    print(write_letter("Yoshi", "Princess Peach"))


def write_letter(receiver, sender):
    return f"""
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Dear {receiver},

    You are cordially invited to a ball at
    Peach's Castle this evening, 7:00 PM.

    Sincerely,
    {sender}
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """

main()
```
<br>

2. Create a list and loop through it (using `i` as an iterator)
```py
def main():
    names = ["Mario", "Luigi", "Daisy", "Yoshi"]

    for i in range(len(names)):
        print(write_letter(names[i], "Princess Peach"))
```
<br>

3. Pythonic simplified alternative syntax (using `name` as an iterator)
```py
def main():
    names = ["Mario", "Luigi", "Daisy", "Yoshi"]
    for name in names:
        print(write_letter(names, "Princess Peach"))
```
