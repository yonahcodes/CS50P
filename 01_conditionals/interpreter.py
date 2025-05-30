def main():
    expression = input("Expression: ").split(" ")
    result = calculate(expression)
    print(result)


def calculate(e):
    operator = e[1]

    if operator == "+":
        result = float(e[0]) + float(e[2])
    elif operator == "-":
        result = float(e[0]) - float(e[2])
    elif operator == "*":
        result = float(e[0]) * float(e[2])
    elif operator == "/":
        result = float(e[0]) / float(e[2])

    return f"{result:.1f}"


main()
