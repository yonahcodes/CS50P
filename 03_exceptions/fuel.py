def main():
    while True:
        try:
            fraction = input("Fraction: ")
            num, deno = fraction.split("/")
            num = int(num)
            deno = int(deno)
            if num <= deno:
                print(f"{percent(num, deno)}")
                break
            else:
                continue
        except (ValueError, ZeroDivisionError):
            pass


def percent(num, deno):
    prct = round(float((num / deno) * 100))
    if prct <= 1:
        return "E"
    elif prct >= 99:
        return "F"
    else:
        return str(prct) + "%"


main()
