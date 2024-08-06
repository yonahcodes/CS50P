import random

def main():
    # Prompt for level
    level = get_level()

    problems = 0
    tries = 0
    score = 0

    for i in range(10):
        # Generate integers for problem
        int_1 = generate_integer(level)
        int_2 = generate_integer(level)
        # Solve and store solution
        solution = int_1 + int_2

        for j in range(3):
            # Prompt user for solution and store
            try:
                answer = int(input(f"{int_1} + {int_2} = "))
                if isinstance(answer, int) and answer == solution:
                    score += 1
                    break
                else:
                    print("EEE")

            except ValueError:
                continue

            if j == 2:
                print(f"{int_1} + {int_2} = {solution}")

        i += 1
    print(f"Score = {score}")


def get_level():
    while True:
        try:
            # Prompt user for a level 1,2 or 3
            level = int(input("Level: "))
            # If level if not an option prompt again
            if level in [1, 2, 3]:
                return level
        # If value is not integer, prompt again
        except ValueError:
            continue


# Generate non-negative integer with digits based on level
def generate_integer(level):
    try:
        if level == 1:
            return random.randint(0, 9)
        elif level == 2:
            return random.randint(10, 99)
        elif level == 3:
            return random.randint(100, 999)
    except ValueError:
        print("Invalid Input")



if __name__ == "__main__":
    main()
