import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()
random_font = random.choice(fonts)

def main():

    if len(sys.argv) == 1:
        s = input("Input: ")
        figlet.setFont(font=random_font)
        print(figlet.renderText(s))
        print(fonts)

    elif len(sys.argv) == 2:
        sys.exit("Invalid usage")

    elif len(sys.argv) == 3:
            if sys.argv[1] == "-f" or sys.argv[1] == "--font" and sys.argv[2] in fonts:
                s = input("Input: ")
                figlet.setFont(font=sys.argv[2])
                print(figlet.renderText(s))
            else:
                sys.exit("Invalid usage")


main()
