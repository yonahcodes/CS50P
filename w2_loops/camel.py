def main():
    camel = split_camel(input("camelCase: "))
    print(snake(camel))


def split_camel(camel):
    # Initialize an empty list for the substrings
    sub_camel = []

    # Initialize an empty list where substrings will be formed (char by char)
    # We also want to initialize the first char
    # knowing that it's the start of the first substring
    current_sub = camel[0]

    # Iterate through chars in the str and check if Uppercase
    # Start iterating from 2nd char str[1:]
    for c in camel[1:]:
        # If char is Uppercase (Meaning everything before forms a sub str)
        if c.isupper():
            # Append current_sub to the sub_camel list
            sub_camel.append(current_sub)
            # Convert new found Uppercase char to lowercase & reset current_sub to it
            current_sub = c.lower()
        else:
            # No Uppercase char found continue iterating and adding chars to current_sub
            current_sub += c

    # No more chars in the str, Append last current_sub to the sub_camel list
    sub_camel.append(current_sub)

    # Return sub_camel list
    return sub_camel


def snake(sub_camel):
    # Join list elements in one string with "_" between them
    return "_".join(sub_camel)


main()
