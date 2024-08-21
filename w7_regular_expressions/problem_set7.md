# CS50P Problem Set 7

## NUMB3RS
An IPv4 address is typically formatted in **dot-decimal notation** as **#.#.#.#**. But each **#** should be a number between `0` and `255`, inclusive.

In a file called `numb3rs.py`, implement a functions called `validate`that expects an **IPv4** address as an input as a **str** and then returns `True` or `False`, respectively, if that input is a valid IPv4 address or not.

Structure `numb3ers.py` as follows, wherein you're welcome to modify `main` and/or implement other functions as you see fit, but you may not import any other libraries, You're welcome, but not required, to use `re` and/or `sys`.
```py
import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    ...

...

if __name__ == "__main__":
    main()
```
<br>

Either before or after you implement `validate` in `numb3ers.py`, additionally implement, in a file called `test_numb3ers.py`, two or more functions that collectively test your implementation of `validate` thoroughly.
<br>

```py
pattern = (r"^([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$")
```
```py
match = re.search(pattern, ip)
```
```py
import pytest
from numb3rs import validate

def test_one_digit():
    assert validate("1.2.3.4") == True
```
<br>