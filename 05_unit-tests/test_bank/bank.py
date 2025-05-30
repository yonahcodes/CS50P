def main():
    while True:
        greeting = input("Greeting: ")
        if not greeting:
            raise ValueError("Please enter greeting")
        print(f"${value(greeting)}")
        break


def value(greeting):
    if greeting.startswith(("hello", "HELLO", "Hello")):
        return 0
    elif greeting.startswith(("h", "H")):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
