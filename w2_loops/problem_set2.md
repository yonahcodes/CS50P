# CS50P - Problem Set 2

## camelCase
Implement a program that prompts the user for the name of a variable in **camel case** and outputs the corresponding name in **snake case**. Assume that the user's input will indeed be in camel case.
```py
for c in list[1:] # Starting at second character
```
```py
list.append(word)
```
```py
.lower()
```
```py
"_".join(list) # Joins list elements into a string with specified separator
```
<br>

## Coke Machine
Coke machine sells a bottle for 50 cents and only accepts 25, 10 and 5 cents.

Implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due.

- Once the user has inputted at least 50 cents, output how many cents in change the user is owed.
- Assume that the user will only input integers, and ignore any integer that isn't accepted
```py
while count < 50:
    …
```
```py
if coin == 25 or coin == 10 …
```
```py
# Ensure the change is not negative
print(f"Change Owed: {count -  50}")
```
<br>

## Just setting up my twttr
Implement a program that prompts the user for a `str` of text and then outputs that same text but with all vowels `A, E, I, O, and U` omitted, whether imputed in uppercase or lowercase.
```py
.append()
```
```py
"".join(list)
```
<br>

## Vanity Plates
Implement a program that prompts the user for a vanity plate and then output `Valid` if it meets all of the requirements or Invalid if it does not.

- Assume that any letters in the user’s input will be uppercase
- `Is_valid()` returns `True` if `s` meets all the requirements and `False` if it does not.
- Assume that `s` will be a `str`
<br>

Requirements:
- Start with at least 2 letters `s[0].isalpha() == False or s[1].isalpha() == False`
- Maximum 6 characters (letters or numbers) `len(6)`
- Minimum 2 characters `len(2)`
- Numbers must come at the end after the letters `if c.isalpha() and i != 0 (range) and s[i - 1].isdigit()`
- First number can't be `0` (`if c == "0"`) and no digit was found before
- No periods, spaces, or punctuation marks `if c.isalnum() == False:`

<br>

```py
zero_digit_found = False
# If current char is a digit equal to zero
# and there was no digit before it (first char is 0) return False
if c.isdigit():
    if c == "0" and zero_digit_found == False:
        return False
    elif c != "0":
        zero_digit_found = True
```
```py
for i, c in enumerate(s)
```
<br>

## Nutrition Facts
Implement a program that prompts users to input a fruit (case-insensitive) and outputs the number of calories in one portion of that fruit, per the FDA’s poster for fruits.
- Assume that users will input fruits exactly as written in the poster.
- Ignore any input that isn't a fruit

```py
dictionary = {"key1": "value1", "key2": "value2"}

if fruit in fruit_dict:
	return fruit_dict[fruit]
```
<br>

> For the function not to return dictionary value: In `main()`, only print `if result != None`
