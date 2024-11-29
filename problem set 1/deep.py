answer = input(
    "What is the Answer to the Great Question of Life, the Universe, and Everything? "
).strip()

if answer == "42":
    print("Yes")
elif answer == "forty-two":
    print("Yes")
elif answer.title() == "Forty Two":
    print("Yes")
elif answer == "forty two":
    print("Yes")
elif answer == "FORTY TWO":
    print("Yes")
else:
    print("No")
