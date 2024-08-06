import inflect

p = inflect.engine()


def main():
    # Initialize list of names
    names = []

    while True:
        try:
            # Prompt user for name
            name = input("Name: ")
            # Append name to list
            names.append(name)
        # User inputs ctrl-d
        except EOFError:
            break

    print()
    print(f"Adieu, adieu, to {p.join(names, final_sep=",")}")


main()
