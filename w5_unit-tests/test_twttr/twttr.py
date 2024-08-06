def main():
    word = input("Input: ").strip()
    print(shorten(word))


def shorten(word):
    vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]

    new_word_list = []

    for c in word:
        if c not in vowels:
            new_word_list.append(c)

    new_word = "".join(new_word_list)
    return new_word


if __name__ == "__main__":
    main()
