def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # Remove the leading $
    fdollars = d.removeprefix("$")
    # Return float amount
    return float(fdollars)


def percent_to_float(p):
    # Remove the trailing % and convert to float
    fpercent = float(p.removesuffix("%"))
    # Return percentage in decimal
    return fpercent / 100


main()
