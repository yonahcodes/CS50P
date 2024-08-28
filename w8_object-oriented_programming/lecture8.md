# CS50P W8 - Object-Oriented Programming
Object-oriented programming (OOP) is a programming paradigm based on the concept of **"objects"**, which can contain data and code: data in the form of **fields** (often known as attributes or properties), and code in the form of **procedures** (often known as methods). In **OOP**, computer programs are designed by making them out of objects that interact with one another.

<br>

1. 
```py
name = input("Name: ")
house = input("House: ")
print(f"{name} from {house}")
``` 
<br>

2. 
```py 
def main():
    name = get_name()
    house = get_house()
    print(f"{name} from {house}")

def get_name():
    return input("Name: ")

def get_house():
    return input("House: ")

if __name__ == "__main__":
    main()
```
<br>

3. `tuple`
```py
def main():
    name, house = get_student()
    print(f"{name} from {house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return name, house

if __name__ == "__main__":
    main()
```
> Notice in this version we are storing the student as a `tuple` (a sequence of values). Unlike a `list`, a `tuple` can't be modified.

<br>

4. 
```py
def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house)


if __name__ == "__main__":
    main()
```
> Notice that we packed that tuple so tht we are able to return both items to a variable called `student`. 

> We are also **indexing** into the tuple using `student[0]` and `student[1]`.

<br>

5. Special case
```py
def main():
    student = get_student()
    if student[0] == "Padma":
        student[1] = "Ravenclaw"
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house)

if __name__ == "__main__":
    main()
```
> Notice that this code produces an error. `'tuple' object does not support item assignment`. Since `tuples` are **immutable**, we are not able to reassign the value of `student[1]`.

<br>

6. `list`
```py
def main():
    student = get_student()
    if student[0] == "Padma":
        student[1] = "Ravenclaw"
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return [name, house]

if __name__ == "__main__":
    main()
```
> If we want to use a `list` instead, to provide some more flexibility, we can change the return value tuple `(name, house)` to a list by putting the return values in brackets `[name, house]`.

<br>

7. `dict`
```py
def main():
    student = get_student()
    print(f"{student['name']} from {student['house']}")

def get_student():
    student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student

if __name__ == "__main__":
    main()
```
> We could also use a `dict` and return two **key-value** pairs. We can now index into the dictionary using the **keys** instead of learning which index number corresponds to which value.

<br>

8. 
```py 
def main():
    student = get_student()
    print(f"{student['name']} from {student['house']}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}

if __name__ == "__main__":
    main()
```
> In this version, we remove the variable student and use `{}` in the return statement to directly create it and return it.

<br>

9. Special case
```py
def main():
    student = get_student()
    if student["name"] == "Padma":
        student["house"] = "Ravenclaw"
    print(f"{student['name']} from {student['house']}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}

if __name__ == "__main__":
    main()
```
<br>

## Classes

