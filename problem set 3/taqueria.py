menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}
keys = menu.keys()
values = menu.values()
total_price = 0


while True:
    try:
        item = input("Item: ").title()
        # checking if the item is in the menu, then adding it's value to total_price

        if item in keys:
            total_price += menu[
                item
            ]  # using the users input as key and extract the corresponding value.
            print("Total: $", end="")
            print("{:.2f}".format(total_price))
    # if item not in menu reprompt the user

    except KeyError:
        pass
    # when the user hits ctrl+d (EOFError) display the total sum

    except EOFError:
        print()
        break
