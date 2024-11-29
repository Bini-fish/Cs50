import sys
from PIL import Image, ImageOps


def main():
    shirt()


def shirt():

    # checking if we have input and output files
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    else:
        pass

    # Checking if input and output extensions are the same
    input_extension = sys.argv[1].split(".")[-1]
    output_extension = sys.argv[2].split(".")[-1]
    if input_extension != output_extension:
        sys.exit("Input and output have different extenstions")

    # checking if the input and output are images
    if input_extension and output_extension not in ["jpg", "png", "jpeg"]:
        sys.exit("Invalid input")
    # cheking if the file exists when opening
    try:
        shirt = Image.open("shirt.png")
        image = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit(f"Could not find {sys.argv[1]}")
    # fits and saves the image to the name in the second argument (output)
    size = shirt.size
    image = ImageOps.fit(image, size)
    image.paste(shirt, mask=shirt)
    image.save(sys.argv[2])
if __name__ == "__main__":
    main()
