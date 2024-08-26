import validators


def main():
    print(validate(input("What's your email address? ")))


def validate(e):
    if validators.email(e):
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()
