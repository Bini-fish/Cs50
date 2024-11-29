import random
import sys
import pyfiglet


figfonts = pyfiglet.FigletFont.getFonts()
random_font = random.choice(figfonts)

if len(sys.argv) == 1:
    text = input("Input: ")
    f = pyfiglet.Figlet(font=str(random_font))
    print(f"Output:\n{f.renderText(text)}")
elif len(sys.argv) == 3:
    font_present = sys.argv[2] in figfonts
    f_present = sys.argv[1] == "-f" or sys.argv[1] == "--font"
    if f_present and font_present:
        text = input("Input: ")
        f = pyfiglet.Figlet(font=sys.argv[2])
        print(f"Output:\n{f.renderText(text)}")
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")
