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

