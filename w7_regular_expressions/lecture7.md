# CS50 W7 - Regular Expressions
Regular expressions or **"regexes"** will enable us to examine **patterns** within our code. They allow us to search, match, and manipulate **strings** based on specific patterns, making them highly useful for tasks like validation, parsing, and text processing.

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

To enhannce our programs functionality, we need to introduce `validation` vocabulary. In **regular expressions** there are **symbols** that allow us to identify **patterns**:
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
# Lecture 00:56:00
