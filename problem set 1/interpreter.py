symbol = input("Expression: ")
splitted = symbol.split()
a = int(splitted[0])
b = int(splitted[2])
z = splitted[1]

if z == "+":
    result = float(a + b)
elif z == "-":
    result = float(a - b)
elif z == "*":
    result = float(a * b)
elif z == "/":
    result = float(a / b)
else:
    print("wrong parameter")
print(f"{result:.1f}")

