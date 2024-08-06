def main():
    txt = input("Input: ").strip()
    print(vowelless(txt))


def vowelless(txt):
    # Define list of vowels to compare chars to
    vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]

    # Initialize empty list for chars of modified str
    new_txt_list = []

    # Iterate through each char
    for c in txt:
        # If not a vowel, it's added to the new char list
        if c not in vowels:
            new_txt_list.append(c)

    # Join elements of the list into a string with no separator ""
    new_txt = "".join(new_txt_list)

    return new_txt


main()
