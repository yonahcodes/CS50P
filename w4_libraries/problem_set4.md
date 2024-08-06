# CS50P - Problem Set 4

## Emojize

Implement a program that prompts the user for a str in English and then outputs the "emojized" version of that str. Converting any codes (:thumbs_up:) or aliases (:thumbsup:) to emoji
<br>

```py
from emoji import emojize
```
```py
s_parts = s.split(" ")
```
```py
result = [ ]
```
```py
for part in parts:
	if ":" in part and "_" in part:
	    result.append(emojize(part, language="alias"))
```
```py
return f"Output: {" ".join(result)}"
```
<br>

## Frank, Ian and Glen’s Letters

Implement a program that zero or two command-line arguments:
- Zero if the user would like to output text in random font.
- Two if the user would like to output text in a **specific font**, in which case the first of the two should be `-f` or `–font`, and the second of the two should be the **name of the font**.

- Prompts the user for a **str** of text
- Outputs that text in desired font

- If the user provides **two** command-line arguments and the first is not **-f** or **–font** or the second is not the name of a font, the program should exit via `sys.exit` with an error message.

<br>

```py
import sys
import random
from pyfiglet import Figlet
```
```py
if len(sys.argv) == n:
    ...
```
```py
sys.exit("Invalid usage")
```
```py
if sys.argv[1] == "-f" or sys.argv[1] == "--font" and sys.argv[2] in fonts:
    ...
```
<br>

## Adieu, Adieu

Implement a program that prompts the user for names, one per line, until the user inputs **cmd-d**. Assume that the user will input at least one name.

Bid adieu to those names: 
- Separating two names with **one and**
- Three names with **two commas** and **one and**
- **n** names with **n-1 commas** and **one and**

<br>

```
"Adieu, adieu, to Liesl"
"Adieu, adieu, to Liesl, and Friedrich"
"Adieu, adieu, to Liesl, Friedrich, and Louisa"
"Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt"
```
<br>

```py
import inflect
p = inflect.engine()
```
```py
names = [ ]
```
```py
try:
    name = input("Name: ")
    names.append(name) 
except EOFError:
    ...
```
```py
print(f"Adieu, adieu to {p.join(names, final_sep=",")}")
```
<br>

## Guessing Game

Prompt user for a level, **n**. 
- If the user does not input a **positive integer**, the program should prompt again.
- Randomly generates an integer between **1** and **n**, inclusive, using the **random** module.

Prompt the user to guess that integer
- If the guess is not positive integer - prompt again
- If the guess is smaller than that integer - output "Too small!"
- If the guess is larger than that integer - output "Too large!"
- If the guess is the same as that integer - output "Just right!"

```py
import random
import sys
```
```py
random.randint(1, n)
```
```py
except ValueError
```
```py
sys.exit()
```
<br>

## Little Professor

Prompt the user for a level **n**
- If the user does not input 1,2 or 3, prompt again

Randomly generate **10 math problems** formatted `X + Y = `. Wherein each of X and Y is a **non-negative integer** with **n** digits. No need to support other operations other than addition (+)

Prompt the user to solve each of those problems
- If an answer is not correct (or not an integer), the program should output **EEE** and prompt the user again. 
- Allow the user up to **three tries** in total for that problem.
- If the user still has not answered correctly after three tries, output the correct answer.

<br>

The program should ultimately output the user’s score: The number of correct answers out of 10.

- `get_level()` to prompt (and if need be re-prompt) the user for a level and return 1, 2 or 3

- `generate_integer()` returns randomly generated non-negative integer with level digits or raises a **ValueError** if level is not 1, 2 or 3
<br>

```py
import random
get_level():
def generate integer(level):
    if level == X:
	return random.randint(0,9)
    … 
```
```py   
for i in range(10):
	for j in range(3):
		answer = int(intput(f"{int_1} + {int_2} =  "))
	        if isinstance(answer, int) and answer == solution:
		        score += 1
		        break
		    else:
                print("EEE")
    if j == 2:
        print(f”{int_1} + {int_2} = {solution}  ”)
i += 1
```
```py
except ValueError
```
<br>

## Bitcoin Price Index
Implement a program that:
- Expects the user to specify as a **command-line argument** the number of Bitcoins, **n**, that they would like to buy.
    - If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.

Queries the **API** for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json which returns a **JSON** object, among whose nested keys is the current price of Bitcoin as a float.
- Be sure to catch any exceptions
- Output the current cost of n Bitcoins in USD to four decimal places, using “,” as a thousands separator
<br>

```py
import json
import requests
import sys
```
```py
r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
r_json = r.json()
return r_json["bpi"]["USD"]["rate_float"]
```
>To access a value inside a dictionary inside another inside another dictionary: `["key1"]["key2"]["key3"]`

```py
except requests.RequestException:
	sys.exit("Error with file")
```
```py
bitcoins = float(sys.argv[1])
```
```py
if __name__ == "__main__":
    main()
```
