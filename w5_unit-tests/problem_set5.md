# CS50P Problem Set 5

## Testing my twttr
Reimplement `twttr.py` from problem 2, restructuring the code:
- `shorten()` expects a **str** as input and returns that same str but with all vowels (A, E, I, O, and U) omitted. Whether inputted in uppercase or lowercase.

Then, in a file called **test_twttr.py** implement one or more functions that collectively test your implementation of shorten thoroughly.
- Each of whose names should begin with **test_**
- Execute your tests with : `pytest test_twttr.py`

<br>

### `twttr.py`
```py
def main():
    word = input("Input: ").strip()
    print(shorten(word))


def shorten(word):
    vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
    new_word_list = []		    

    for c in word:
	    if c not vowels:
		    new_word_list.append(c)
				
    new_word = "".join(new_word_list)
    			    return new_word


if __name__  == "__main__":
    main()
```
<br>

### `test_twttr.py`
```py
import pytest
from twttr import shorten

def test_alpha_lower():
    assert shorten("twitter") == "twttr"
    assert shorten("lazer") == "lzr"


def test_alpha_upper():
    assert shorten("GOOGLECHROME") == "GGLCHRM"
    assert shorten("TEST") == "TST"


def test_alphanum():
    assert shorten("cs50") == "cs50"
    assert shorten("Hai18") == "H18"


def test_punctuation():
    assert shorten("Bar.Yohai") == "Br.Yh"
    assert shorten("Hallo!") == "Hll!"
```
<br>


## Back to the Bank

Reimplement Home Federal Saving Bank from Problem Set 1 `bank.py`:

- **value()** expects a str as input and returns an int
    - Namely 0 if that str starts with `"hello"`, 20 if it starts with an `"h"`, or 100 otherwise
    - Treat the str case-insensitively.

- Assume that the string passed to value() will not contain leading spaces
Only main should call print

Then, in a file called `test_bank.py` implement **3** or more functions that collectively test your implementation of value() thoroughly.
- Each of whose names should begin with `test_`
- Execute your tests with : `pytest test_bank.py`

<br>

### `bank.py`
```py
def main():
    while True:
        greeting = input("Greeting: ")
	    if not greeting:
	        raise ValueError("Please enter greeting")
        print(f"${value(greeting)}")
        break


def value(greeting):
	if greeting.startswith(("hello", "HELLO", "Hello")):
	    return 0
	elif greeting.startswith(("h", "H")):
	    return 20
	else:
	    return 100


if __name__  == "__main__":
    main()
```

<br>

### `test_bank.py`
```py
import pytest
from bank import value


def test_lower():
    assert value("hello patrick") == 0
    assert value("herrow") == 20
    assert value("skamlikum") == 100


def test_upper():
    assert value("HELLO BRO") == 0
    assert value("HERROW MALFOY") == 20
    assert value("S'UP") == 100


def test_up_low():
    assert value("Hello!") == 0
    assert value("hErrOW jUdE") == 20
    assert value("Ello Bro") == 100
```
<br>

## Re-requesting a Vanity Plate
Reimplement Vanity Plate from Problem Set 2 `plates.py`

- **is_valid()** expects a str as input. Returns **True** if that str meets all requirements. Returns **False** if it does not.
- **main()** only called if __name__ == “”__main__

Then, in a file called `test_plates.py` implement 4 or more functions that collectively test your implementation of is_valid() thoroughly.
- Each of whose names should begin with **test_**
- Execute your tests with : `pytest test_plates.py`

<br>

### `plates.py`

```py
def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    zero_digit_found = False
    if len(s) < 2 or len(s) > 6 or s[0].isalpha() == False 
    or s[1].isalpha() == False:
        return False

    for i, c in enumerate(s):
        if c.isalnum() == False:
            return False
        if c.isdigit():
            if c == "0" and zero_digit_found == False:
                return False
            elif c != "0":
                zero_digit_found = True

        if c.isalpha() and i != 0 and s[i - 1].isdigit():
            return False
    return True


if __name__ == "__main__":
    main()
```

<br>

### `test_plates.py`
```py
import pytest
from plates import is_valid

def test_starts_2_letters():
    assert is_valid("HELLO") == True
    assert is_valid("AE332") == True
    assert is_valid("A3356") == False
    assert is_valid("5566O") == False


def test_min_2_characters():
    assert is_valid("H") == False
    assert is_valid("AA") == True
    assert is_valid("5") == False
    assert is_valid("AA5") == True


def test_max_6_letters():
    assert is_valid("LAZERY") == True
    assert is_valid("GOODBYE") == False
    assert is_valid("EMET26") == True
    assert is_valid("OK84567") == False


def test_number_placement():
    assert is_valid("AA1826") == True
    assert is_valid("AAA222") == True
    assert is_valid("CS50P") == False
    assert is_valid("ZZ44TP") == False


def test_zero_placement():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False

def test_special_characters():
    assert is_valid("HELLO, WORLD") == False
    assert is_valid("PI3.14") == False
    assert is_valid("YO700!") == False
```
<br>

## Refueling
Reimplement Fuel Gauge from Problem Set 2 `fuel.py`

**convert()** expects a str in `X/Y` format input
- Each of X and Y is an integer
- Returns that fraction as a **percentage** rounded to the nearest int between 0 and 100 inclusive.
- If X and/or Y is not an integer, or if X is greater than Y, then convert should raise a ValueError.
- If Y is 0 then convert should raise a ZeroDivisionError.

**gauge()** expects an int and returns a str that is:
- "E" if that int is less than or equal to 1
- "F" if that int is greater than or equal to 99
- 2Z%" otherwise, where Z is that same int

<br>

Then, in a file called `test_fuel.py` implement 2 or more functions that collectively test your implementation of convert() and gauge() thoroughly.
- Each of whose names should begin with **test_**
- Execute your tests with : `pytest test_plates.py`

### `fuel.py`
```py
def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))

def convert(fraction):
    try:
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)

        if y == 0:
            raise ZeroDivisionError("Denominator should be greater than 0")
        if x > y:
            raise ValueError("Numerator should not be greater than denominator")

    except ValueError:
        raise ValueError("Please enter integer values")

    return round((float(x / y) * 100))


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(percentage) + "%"


if __name__ == "__main__":
    main()
```
<br>

### `test_fuel.py`
```py
import pytest
from fuel import convert, gauge

def test_convert():
    assert convert("3/4") == 75
    assert convert("1/4") == 25

def test_convert_exceptions():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")
    with pytest.raises(ValueError):
        convert("three/four")
    with pytest.raises(ValueError):
        convert("1.5/3")

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(25) == "25%"
    assert gauge(75) == "75%"
```
