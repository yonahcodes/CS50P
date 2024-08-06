def convert(s):
    if ":(" in s:
        s = s.replace(":(", "🙁")
    if ":)" in s:
        s = s.replace(":)", "🙂")
    return s


def main():
    s = input("Enter string: ")
    new_s = convert(s)
    print(new_s)


main()
