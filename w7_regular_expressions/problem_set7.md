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
import re
import sys
```
```py
pattern = (r"^([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$")
```
```py
match = re.search(pattern, ip)
```
```py
import pytest
from numb3rs import validate
```
```py
def test_one_digit():
    assert validate("1.2.3.4") == True
```
<br>

## Watch on YouTube
In a YouTube video, if you click **Share**, then **Embed**, you will see the **HTML** code that you can copy into your own website's source code.

```
<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```
> `iframe` is an **HTML** "element", and `src` is one of several HTML "attributes" therein, the value of which, between quotes, is the URL of the video.

<br>

Because some HTML attributes are optional, you could instead minimally embed:
```
<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
```
<br>

Suppose that you’d like to extract the URLs of YouTube videos that are embedded in pages (e.g., https://www.youtube.com/embed/xvFZjo5PgG0), converting them back to shorter, shareable youtu.be URLs (e.g., https://youtu.be/xvFZjo5PgG0) where they can be watched on YouTube itself.

<br>

Implement a function called `parse` that expects a `str` of HTML as input, extracts any YouTube URL that's the value of a `src` attribute of an `iframe` element, and returns its shorter, shareable `youtu.be` equivalent as a `str`. 

- Expect that any such URL will be in one of the formats below.
- Assume that the value of `src` will be surrounded by double quotes.
- Assume that the input will contain no more than one such URL.
- If the input does not contain any such URL at all, return `None`.

<br>

```
http://youtube.com/embed/xvFZjo5PgG0
https://youtube.com/embed/xvFZjo5PgG0
https://www.youtube.com/embed/xvFZjo5PgG0
``` 
<br>

Structure `watch.py` as follows, wherein you're welcome to modify `main` and/or implement other functions as you see fit, but you may not import any other libraries. You are welcome, but not required, to use `re` and/or `sys`.
```py
import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    ...

...

if __name__ == "__main__":
    main()
```
Main
```py
if matches := re.search(r'src="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)"', s):
    return f"https://youtu.be/{matches.group(1)}"
```
<br>

## Working 9 to 5

Most countries use a **24-hour** clock, the United States tends to use a **12-hour** clock. Instead of `09:00 to 17:00`, many Americans would say `9:00 AM to 5:00PM` ("AM" is an abbreviation for "ante meridiem" and "PM" is an abbreviation of "post meridiem", "meridiem" means midday or noon).

Just as `12:00 AM` in 12-hour format would be `00:00` in 24-hour format, so would `12:01 AM` through `12:59 AM` be `00:01` through `00:59`, respectively.

<br>

In a file called `working.py`, implement a function called `convert` that expects a `str` in any of the 12-hour formats below and returns the corresponding `str` in 24-hour format.
- Expect that **AM** and **PM** will be capitalized (with no periods) and that there will be a space before each.
- Assume that these times are representative of actual times.
```
9:00 AM to 5:00 PM
9 AM to 5 PM
9:00 AM to 5 PM
9 AM to 5:00 PM
```
<br>

- Raise a `ValueError` instead if the input to `convert` is not either of those formats or if either time is invalid (e.g., 12:60 AM, 13:00 PM, etc.).
- Do not assume that someone's hours will start ante meridiem and end post meridiem.

<br>

Either before or after you implement convert in `working.py`, additionally implement, in a file called `test_working.py`, three or more functions that collectively test your implementation of convert thoroughly.

<br>
