def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Initialize flag variable for digit 0
    zero_digit_found = False

    # If length of plate is not between 2 and 6,
    # or if first two characters are not letters, return False
    if len(s) < 2 or len(s) > 6 or s[0].isalpha() == False or s[1].isalpha() == False:
        return False

    # Iterate through each index and char
    for i, c in enumerate(s):
        # If any char is not alphanumeric, return False
        if c.isalnum() == False:
            return False

        # If current char is a digit equal to zero
        # and there was no digit before it (first char is 0) return False
        if c.isdigit():
            if c == "0" and zero_digit_found == False:
                return False
            elif c != "0":
                zero_digit_found = True

        # If any char is a letter and is preceded by a digit, return False
        if c.isalpha() and i != 0 and s[i - 1].isdigit():
            return False

    return True


if __name__ == "__main__":
    main()

