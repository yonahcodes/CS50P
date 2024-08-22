import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if match := re.search(r'src="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)"', s):
        return f"https://youtu.be/{match.group(1)}"


if __name__ == "__main__":
    main()
