# CS50 W7 - Regular Expressions
Regular expressions or **"regexes"** will enable us to examine **patterns** within our code. They allow us to search, match, and manipulate **strings** based on specific patterns, making them highly useful for tasks like validation, parsing, and text processing. https://docs.python.org/3/library/re.html

<br>

1. 
```py
email = input("What's your email? ").strip()

if "@" in email:
    print("Valid")
else:
    print("Invalid")
```
> This code appears to work but it actually broken. One could input `@@` alone and the input could be regarded as valid.

<br>

2. 
```py
email = input("What's your email? ").strip()

if "@" in email and "." in email:
    print("Valid")
else:
    print("Invalid")
```
> This code looks for `@` and a `.` in order to validate the email address, but again, is still not robust enough as an input of `@.`will be validated. 

<br>

3. 
```py
email = input("What's your email? ").strip()

username, domain = email.split("@")

if username and "." in domain:
    print("Valid")
else:
    print("Invalid")
```
> The `strip()` method is used to split the string at the `@` and assign first part to `username` variable and second part to `domain` variable.

>`if username` determines if `username` exists, and `"." in domain` checks for a `.` in domain.

<br>

4. 
```py
email = input("What's your email? ").strip()

username, domain = email.split("@")

if username and domain.endswith(".edu"):
    print("Valid")
else:
    print("Invalid")
```
> `endswith()` method will check if domain contains `.edu`. However, an input of `malan@.edu` would be considered valid.

<br>

We could keep iterating through this code manually. However, Python `re` library has built-in functions that can validate user inputs against patterns.

<br>

## Regular expression operations library - `re`

<br>

1. 
```py
import re

email = input("What's your email? ").strip()

if re.search("@", email):
    print("Valid")
else:
    print("Invalid")
```
> Notice that we are only checking for the presence of `@`in the `email`, which is no progress for now.

> The `search` library follows the signature `re.search(pattern, string, flags=0)`.

<br>

To enhance our programs functionality, we need to introduce `validation` vocabulary. In **regular expressions** there are **symbols** that allow us to identify **patterns**:
```
.   any character except a new line
*   0 or more repetitions
+   1 or more repetitions
?   0 or 1 repetition
{m} m repetitions
{m,n} m-n repetitions
```
<br>

2. 
```py
import re

email = input("What's your email? ").strip()

if re.search(".+@.+", email):
    print("Valid")
else:
    print("Invalid")
```
> In **".+@.+"**, `.+` is used to determine if at least one or more characters are present to the **left** and to the **right** of the `@`. 

<br>

3. 
```py
import re

email = input("What's your email? ").strip()

if re.search(".+@.+.edu", email):
    print("Valid")
else:
    print("Invalid")
```
> Notice here that we added a check `.edu` but the result will not be the one expected. In this context `.` means **any character** and not an actual `.`

<br>

We can use the **escape character** `\` to include the `.` in our **string** instead of our validation expression:
```py
if re.search(".+@.+\.edu", email):
    print("Valid")
```
> Python might misinterpret the use of `\.` as an escape sequence similar to `\n`. To solve this we can use `raw strings`.

<br>

### `raw strings`
**raw strings** are strings that don't format special characters. Placing an `r` in front of a string tells the Python interpreter to take each character of the string at face-value. (`r"\n"` would be considered `\` and `n` instead of new line).
<br>

4. 
```py
import re

email = input("What's your email? ").strip()

if re.search(r".+@.+\.edu", email):
    print("Valid")
else:
    print("Invalid")
```
> We still have a problem. User could input `My email address is malan@harvard.edu.` and it would be considered valid. 

<br>

To address this, we need to include more validation special symbols:
```
^   matches the start of the string
$   matches the end of the string or just before the newline at the end of the string
```
<br>

5. 
```py
import re

email = input("What's your email? ").strip()

if re.search(r"^.+@.+\.edu$", email):
    print("Valid")
else:
    print("Invalid")
```
> Now, this version would render **Invalid** the input `My email is malan@harvard.edu.` because the **regular expression** expects `"u"`to be the last character of the input.

> Users could still type as many `@` symbols as they wish. `malan@@@harvard.edu` would be considered valid.

<br>

We can can add symbols to our regular expression to address this problem:
```
[]    set of characters
[^]   complementing the set
```
<br>

6. `[^]`
```py
import re

email = input("What's your email? ").strip()

if re.search(r"^[^@]+@[^@]+\.edu$", email):
    print("Valid")
else:
    print("Invalid")
```
> Notice that `[^@]+` means any 1 or more characters except an `@`. This means that before and after the `@` the **regular expression** only accepts characters that are not `@`.

<br>

7. `[]`
```py
import re

email = input("What's your email? ").strip()

if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
    print("Valid")
else:
    print("Invalid")
```
> Notice that **set of characters** `[a-zA-Z0-9_]` tells the validation that characters must be between `a` and `z`, between `A` and `Z`, between `0` and `9` and potentially include an `_` symbol.

<br>

To simplify this process, common patterns have been built into regular expressions by other programmers:

8. 
```py
import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@\w+\.edu$", email):
    print("Valid")
else:
    print("Invalid")
```
> Notice that `\w` is the same as `[a-zA-Z0-9_]`.

<br>

Additional patterns:
```
\d    decimal digit
\D    not a decimal digit
\s    whitespace characters
\S    not a whitespace character
\w    word character, as well as numbers and the underscore
\W    not a word character
```
<br>

9. Include more `Top-Level Domains`
```py
import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@\w+\.(com|edu|gov|net|org)$", email):
    print("Valid")
else:
    print("Invalid")
```
> Notice that in `(com|edu|gov|net|org)`, the `|` means `or` and `(...)` is used to group them together.

```
A|B     either A or B
(...)   a group
(?:...) non-capturing version
```
<br>

## Case Sensitivity - `flags=`

Recall that within the `re.search` function, there is a parameter for flags **re.search(pattern, string, `flags=0`)**. 

Some built-in flag variables:
```
re.IGNORECASE
re.MULTILINE
re.DOTALL
```
<br>

10. `re.IGNORECASE`
```py
import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
```
> The input `MALAN@HARVARD.EDU` would now be valid.

<br>

11. `?`

Notice that the email address `malan@cs50.harvard.edu` would be considered invalid because of the additional `.` 
```py
import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
```
> In this version we added a new grouped expression `(\w+\.)?`, that means to accept an alphanumeric character or underscore (`\w1`), 1 or more times (`+`), and a literal dot (`.`), followed by the `?` quantifier, that makes the entire group optional. (Remember that the symbol `?`, means 0 or 1 repetitions.)

> Now inputs `malan@cs50.harvard.edu` and `malan@harvard.edu` are considered valid.

<br>

The full **regular expression** used by most browsers to validate email addresses is far more complicated than the one we implemented. It looks like this:
```
^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$`
```
Thankfully, we can, and should, take advantage of **libraries** built by experienced programmers that simplify the process of validating an email address.

<br>

## Cleaning Up User Input

<br>

1. `format.py`
```py
name = input("What's your name? ").strip()
print(f"hello, {name}")
```
> This program expects users to input their names. The user could input their name in whatever order they decide (`Malan, David`). This could make it difficult to **standardize** how names are stored and used by our program.

<br>

2. 
```py
name = input("What's your name? ").strip()

if "," in name:
    last, first = name.split(", ")
    name = f"{first} {last}"

print(f"hello, {name}")
```
> `last, first = name.split(", ")` is run if there's a `,` in the name. The name is then standardized as **first** and **last**.

> If the user enters `Malan,David` with no spaces, the compiler will throw and error.

<br>

3. `()` - `.groups()`
```py
import re

name = input("What's your name? ").strip()
matches = re.search(r"^(.+), (.+)$", name)

if matches:
    last, first = matches.groups()
    name = f"{first} {last}"

print(f"hello, {name}")
```
> The grouping symbol `(...)` has the capability of **capturing** the matching expression entered by the user. `re.search` can return those sets of matches, which we stored in the variable `matches`.

> `last, first = matches.groups()` then accesses those values (`matches.groups()`) and assigns them to variables `last` and `first`.

<br>

4. `.group(n)`
```py
import re

name = input("What's your name? ").strip()
matches = re.search(r"^(.+), (.+)$", name)

if matches:
    name = matches.group(2) + " " + matches.group(1)
    
print(f"hello, {name}")
```
> Notice in this version we are requesting specific groups using singular `.group()` and **concatenating** them with a single space `" "` in the order we wanted.

> `group(1)` is the first to appear, at the left of the comma.

Now, we are still expecting a space after the comma as per `(.+), (.+)`. An input of `Malan,David` will not return the expected result. 

<br>

5. `*`
```py
import re

name = input("What's your name? ").strip()
matches = re.search(r"^(.+), *(.+)$", name)

if matches:
    name = matches.group(2) + " " + matches.group(1)
    
print(f"hello, {name}")
```
> Notice the addition of the `*` (0 or more repetitions) in our validation statement. Now the code will accept no spaces `Malan,David` or many spaces `Malan,    David`.

<br>

6. **walrus operator** `:=`
```py
import re

name = input("What's your name? ").strip()
if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)
    
print(f"hello, {name}")
```
> Notice the use of the **walrus operator** `:=`. This operator allows us to combine two lines of code by **assigning a value** from right to left and **ask a Boolean question** at the same time.

<br>

## Extracting User Input

<br>

Let's build a program that extracts some specific information form user input.

1. `twitter.py`
```py
url = input("URL: ").strip()
print(url)
```
> Notice that if we type URL `https://twitter.com/davidjmalan`, it prints exactly what the user typed.

<br>

2. `replace()`
```py
url = input("URL: ").strip()

username = url.replace("https://twitter.com/", "")
print(f"Username: {username}")
```
> Notice the use of `replace()` method, which allows us to find part of the URL and replace it with nothing `""`.

This could still be problematic if user only enters `twitter.com` instead of including the full expected format.

If user enters `My URL is https://twitter.com/davidjmalan`, the output will be `My URL is davidjmalan`.

<br>

3. `removeprefix()`
```py
url = input("URL: ").strip()

username = url.removeprefix("https://twitter.com/")
print(f"Username: {username}")
```
> The `removeprefix()` method does not resolve our problem but does simplify the removal of the **url** and anything that precedes it.

<br>

4. `re.sub()`

Within the `re` library, there is a method called `sub` that allows us to substitute a pattern with something else.

`re.sub(pattern, repl, string, count=0, flags=0)`.
```py
import re

url = input("URL: ").strip()

username = re.sub(r"https://twitter.com/", "", url)
print(f"Username: {username}")
```
> This version of the code uses the **regular expressions** way to substitute elements but still does not cover all input variations. Also, the `.` could be interpreter improperly by the compiler.

<br>

5. 
```py
import re

url = input("URL: ").strip()

username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
print(f"Username: {username}")
```
- `^` caret was added to signal the beginning od the match
- `\` was added to all the dots `.`
- `?` was added after `https` making the "s" optional to tolerate `http`
- `(www\.)?` Was added to accept the option of including "www."
- `(https?:\\)?` Grouping and making not only the `s` optional with `?` but also the whole protocol.

<br>

> Still, we are blindly expecting that the user inputted a **url** that matches the pattern and has a **username**.

<br>

6. `re.search()`
```py
import re

url = input("URL: ").strip()

matches = re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
if matches:
    print(f"Username:", matches.group(2))
```
> Notice now, how we are capturing the end of the URL using `(.+)$` regular expression and only returning it (`matches.group(2)`) **if** the user's input matches our regular expression.

> Notice the importance of respecting the order of the **groups**. Using `matches.group(1)` will return `www.` if included in the input or `None` if not included.

<br>

7. `(?:...)`
```py
import re

url = input("URL: ").strip()

matches = re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
if matches:
    print(f"Username:", matches.group(1))
```
> Notice here that adding `?:` at the beginning of the **group** `(?:www\.)` will tell the compiler not to **capture** and only group the expression, so that we could access the first (and only) **captured** group `(.+)` with `matches.group(1)`.

<br>

8. **walrus operator** `:=`
```py
import re

url = input("URL: ").strip()

if matches := re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))
```

<br>

9. `[]`
```py
import re

url = input("URL: ").strip()

if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)$", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))
```
> Notice in this version that we used `([a-z0-9_]+)` to only accept twitter's valid username format.

<br>

## `groups.py`
Program that validates international phone numbers.

<br>

1. 
```py
import re

# Dictionary of country codes and corresponding countries
locations = {"+1": "United States and Canada", "+62": "Indonesia", "+505": "Nicaragua"}

def main():
    # Define the pattern for the expected phone number format
    # using a raw string regular expression
    pattern = r"\+\d{1,3} \d{3}-\d{3}-\d{4}"

    # Prompt user for a phone number input and store in variable "number"
    number = input("Number: ")

    # Use the re.search() function to check if input matches the pattern
    # and store result (match object) in the match variable
    match = re.search(pattern, number)
    
    if match:
        # If the input matches the pattern, print "Valid"
        print("Valid")
    else:
        # If the input does not match the pattern, print "Invalid"
        print("Invalid")


if __name__ == "__main__":
    main()
```
```
r"\+\d{1,3} \d{3}-\d{3}-\d{4}"
```
- `\+` means to treat the plus sign `+` literally.
- `\d` means decimal digit
- `{1,3}` means 1 to 3 repetitions

<br>

2. Capture groups `()`
```py
import re

locations = {"+1": "United States and Canada", "+62": "Indonesia", "+505": "Nicaragua"}

def main():
    # Add capture group for the country codes "(\+\d{1,3})"
    pattern = r"(\+\d{1,3}) \d{3}-\d{3}-\d{4}"
    number = input("Number: ")

    match = re.search(pattern, number)

    if match:
        # Access the first capture group and store in `country_code`
        country_code = match.group(1)

        # Print country code
        print(country_code)
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
```
<br>

3. Using capture group as key to access value in dictionary
```py
import re

locations = {"+1": "United States and Canada", "+62": "Indonesia", "+505": "Nicaragua"}

def main():
    # Add capture group for the country codes "(\+\d{1,3})"
    pattern = r"(\+\d{1,3}) \d{3}-\d{3}-\d{4}"
    number = input("Number: ")

    match = re.search(pattern, number)

    if match:
        # Access the first capture group and store in `country_code`
        country_code = match.group(1)

        # Retrieve and print country corresponding to country code 
        print(locations[country_code])
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
```
> Notice the use of `country_code` as a key to access corresponding value (country)

<br>

4. Naming capture group for better access
```py
import re

locations = {"+1": "United States and Canada", "+62": "Indonesia", "+505": "Nicaragua"}

def main():
    # Naming capture group pattern for easy access
    pattern = r"(?P<country_code>\+\d{1,3}) \d{3}-\d{3}-\d{4}"
    number = input("Number: ")

    match = re.search(pattern, number)

    if match:
        # Access the capture group with its name "country_code"
        country_code = match.group("country_code")

        # Retrieve and print country corresponding to country code
        print(locations[country_code])
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
```
> Notice the syntax to name a capture group within a regular expression `(?P<name>...)`

<br>

## `code.py`

A Hexadecimal color code:
- Begins with #
- Is composed of 6 characters
- 0-9 and A-F (or a-f)

<br>

Examples:
```
Black: #000000 
White: #FFFFFF
Red: #FF0000
Blue: #0000FF
Green: #00FF00
```
<br>

Program that validates Hexadecimal color codes
```py
import re


def main():
    # Prompt user for color code
    code = input("Hexadecimal color code: ")

    # Define the pattern for the expected hexadecimal color code
    # using a raw string regular expression
    pattern = r"^#[a-fA-F0-9]{6}$"

    # Use the re.search() function to check if input matches the pattern
    # and store result (match object) in the match variable
    match = re.search(pattern, code)

    if match:
        # If the input matches the pattern, print Valid and what it matched with
        print(f"Valid. Matched with {match.group()}")
    else:
        # If the input does not match the pattern, print "Invalid"
        print("Invalid")


if __name__ == "__main__":
    main()
```
```
r"^#[a-fA-F0-9]{6}$"
```
- `^#` means that `#` must be the first character of the input 
- `[a-fA-F0-9]` determines the set of characters (ranges) accepted 
- `{6}` means 6 repetitions
- `$` means that the last characters must be the `{6}` characters in the range of pattens.
