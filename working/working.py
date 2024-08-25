import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        pattern = r"^(1[0-2]|[1-9]):?([0-5][0-9])?\s(AM|PM)\sto\s(1[0-2]|[1-9]):?([0-5][0-9])?\s(AM|PM)$"

        if match := re.search(pattern, s):

            if not "12" in match.group(1) and "PM" in match.group(3):
                hours1 = int(match.group(1)) + 12
            elif "12" in match.group(1) and "AM" in match.group(3):
                hours1 = 00
            else:
                hours1 = int(match.group(1))

            minutes1 = match.group(2) if match.group(2) else "00"

            if not "12" in match.group(4) and "PM" in match.group(6):
                hours2 = int(match.group(4)) + 12
            elif "12" in match.group(4) and "AM" in match.group(6):
                hours2 = 00
            else:
                hours2 = int(match.group(4))

            minutes2 = match.group(5) if match.group(5) else "00"

            return f"{hours1:02}:{minutes1} to {hours2:02}:{minutes2}"

        else:
            raise ValueError("Invalid time format")

    except ValueError:
        raise ValueError("Invalid time format")


if __name__ == "__main__":
    main()
