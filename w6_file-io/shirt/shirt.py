import os
from PIL import Image, ImageOps
import sys

def main():
    try:
        # Ensure correct number of command-line arguments (2)
        if len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")

        # Assign c-l arguments (img files) to variables
        input_img = sys.argv[1]
        output_img = sys.argv[2]

        # Ensure files have supported extensions
        extensions = [".jpg", ".JPG", ".jpeg", ".JPEG", ".png", ".PNG"]

        if not any(input_img.endswith(ext) for ext in extensions):
            sys.exit("Invalid input")
        if not any(output_img.endswith(ext) for ext in extensions):
            sys.exit("Invalid output")

        # Ensure input and output files extensions match
        if os.path.splitext(input_img)[1] != os.path.splitext(output_img)[1]:
            sys.exit("Input and Output have different extensions")

        shirtify(input_img, output_img)

    # Handle file not found error
    except FileNotFoundError:
        sys.exit("File not found")


def shirtify(input_img, output_img):
    try:
        # Open the images
        with Image.open(input_img) as image, Image.open("shirt.png") as shirt:
            # Resize the input image to fit shirt size
            size = shirt.size
            image = ImageOps.fit(image, size)

            # Paste the shirt image onto the resizer input image using shirt as a mask
            image.paste(shirt, (0, 0), shirt)

            # Save final image
            image.save(output_img)

    except FileNotFoundError:
        raise FileNotFoundError("File not found")


if __name__ == "__main__":
    main()
