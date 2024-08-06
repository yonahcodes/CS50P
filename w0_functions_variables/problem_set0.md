# CS50P - Problem Set 0 

## Indoor Voice
- Prompt for input and output sale input in lowercase
- Punctuation and whitespace unchanged
- define and call `main()` 
- `lower()`
<br>

## Playback Speed
Prompt user for input and output, same input replacing spaces with "..." 
- replace(old, new)
- replace(" ", "...")
<br>

## Making Faces
Implement a function called `convert()` that accepts a str as input and returns the same input with any `:)` converted to a 🙂 emoji (:slightly-happy:) and any `:(` converted to 😕(:slightly-frowning:)

Implement a function called `main()` that prompts the user for input, calls `convert()` on that input, and prints the result.
```python
s = s.replace(":(", "😕")
```
<br>

## Einstein
`E=mc2` (**E = energy (in Joules), m = mass (kilograms), c = speed of light (approx. 300 000 000 meters per second)**).

Implement a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. 
- Assume that the user will input an integer.
```python
pow(number, exponent)
```
<br>

## Tip Calculator
Implement a function `dollar_to_foat()` that accepts a str as input (formatted `$##.##`, where each # is a decimal digit). Remove the leading `$`, and return the amount as a `float`.($50.00 should return 50.0)


Implement a function `percent_to_float()` that accepts a str as input (formatted `##%`, where each # is a decimal digit), remove the trailing `%`, and return the percentage as a `float`. (15% should return 0.15)
```python
str.removeprefix("$")

str.removesuffix("%")

float()
```
