def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


# converting the dollar amount entered in to a decimal number


def dollars_to_float(d):
    splitted = d.split("$")
    number = float(splitted[1])
    return number


# converting the percentage entered in to a decimal number


def percent_to_float(p):
    splitted = p.split("%")
    number = float(splitted[0])
    return number / 100


main()
