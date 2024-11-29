item = input("Item: ")
Calories = 0
if item == "apple":
    Calories = 130
    print(f"Calories: {Calories}")
elif item == "banana":
    Calories = 110
    print(f"Calories: {Calories}")
elif item == "Avocado":
    Calories = 50
    print(f"Calories: {Calories}")
elif item == "Sweet Cherries" or item == "pear":
    Calories = 100
    print(f"Calories: {Calories}")
elif item == "Kiwifruit":
    Calories = 90
    print(f"Calories: {Calories}")
else:
    pass
