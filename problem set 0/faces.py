expression = input()
expression = expression.split(" ")
face = expression[1]
length = len(expression)

if length <= 2:
    if face == ":)":
        print(f"{expression[0]} 🙂")
    elif face == ":(":
        print(f"{expression[0]} 🙁")
    else:
        pass
else:
    print(f"{expression[0]} 🙂 {expression[2]} 🙁")
