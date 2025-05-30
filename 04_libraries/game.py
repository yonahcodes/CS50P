import random
import sys


def main():
    while True:
        try:
            n = int(input("Level: "))
            if n > 0:
                random_int = random.randint(1, n)
                break
        except ValueError:
            continue

    while True:
        try:
            guess = int(input("Guess: "))
            if guess <= 0:
                continue
            if guess < random_int:
                print("Too small!")
            elif guess > random_int:
                print("Too large!")
            else:
                print("Just right!")
                sys.exit()
        except ValueError:
            continue

main()
