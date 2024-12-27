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
<br><br>

3. `tuple`: Ordered collection of items that are **immutable**.
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

<br><br>

6. `list`: Ordered collection of items that are **mutable**.
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

<br><br>

7. `dict`: Collection of **key-value pairs** where each key is unique. They are **unordered** and **mutable**.
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

In object-oriented programming (OOP), a `class` is a blueprint or template for creating objects. It defining their `attributes` (data) and `methods` (functions). Python **classes** allow us to create data structures, define their behavior and give them a **name**.

[Python docs](https://docs.python.org/3/tutorial/classes.html)

<br>

1. 
```py
class Student:
    ...


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")
    return student


if __name__ == "__main__":
    main()
```
> A defined class, even when not implemented, can be used in the code.

<br>

- On top of the file, we created a **class** called `Student` (Capitalized for convention) that we are going to implement later.

- `student = Student()` creates a **object** `student` of class `Student`.

-  `student.name` and `student.house`: We used **"dot notation"** to access *attributes* (name and house) of this variable `student` of class `Student`.

<br>

### Constructor Method

2. `__init__`
```py
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)
    return student


if __name__ == "__main__":
    main()
```
> In this version we are standardizing how we pass in data to the  `Student` class. This give us more control and ability to error check.

- `student = Student(name, house)` is a "Constructor call". It is calling the **function** within `class Student` with the objectif of using it's structure and customizing it by passing to it the variables `name` and `house`. The return value of calling the function is then assigned to, and in the process, creating the object `student`.

- `def __init__(self, name, house):` Defines the **function** to be called within the **class**, by convention, using the `__init__` **constructor method**. It is called when creating a new object of the class and initializes the object's attributes, The first parameter is always `self` and is used to define the **instance variables**.

- `self.name = name` Creates instance variable `name` and store the value of variable `name` to it in the **object**. (same goes for `self.house = house`).

<br>

**Let's identify each concept:** 
### Objects
When we create a **class** and use it to generate something, we create an **"object"** or an **"instance"**. In our code, `student` is an object.

In **OOP**, an **object** is an **instance** of a **class**. It represents a specific entity that has the **attributes** (data) and **behavior** (methods) defined in the **class**.

- `student = Student(name, house)` creates an object of the Student class.

- `student is an object (instance)` of the Student class.

<br>

### Instance Methods
An **instance method** is a type of method defined inside a **class** that can access and modify the **attributes** of a specific **object**.

- `__init__(self, name, house)` is an instance method of the Student class.

- It's called automatically when a new Student object is created.

- The `self` parameter refers to the instance being created.

<br>

### Instance variables
**Instance variables** are **attributes** are defined within **methods** of a class. They store data that can vary between different **objects** (instances) of the same class.

- `self.name` is an instance variable of the Student class.

- `self.house` is another instance variable of the Student class.

- These are created and initialized within the `__init__` method.

<br>

3. Simplified
```py
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()
```
> Notice how `return Student(name, house)` removes the need to assign it to `student`. The line `student = get_student()` in the `main()` function calls `get_student()` which returns an **object** which is then assigned to `student`.

<br>

## `raise`
**Object-oriented programming** encourages you to encapsulate all the functionality of a class, including error checking, within the class definition.

4. 
```py
class Student:
    def __init__(self, name, house):
        
        # If name is blank
        if not name:
            raise ValueError("Missing name")
        # If house is not valid
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        
        self.name = name
        self.house = house


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

if __name__ == "__main__":
    main()

```
> The `raise` keyword is used to **raise an exception**. We can define the kind of error to raise and the text to print to the user.

<br>

Lecture 1:03:00
