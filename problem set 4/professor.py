import random


def main():
    number = get_level()
    generate_integer(number)


def get_level():
    while True:
        try:
            number = int(input("Level: "))
            if number in range(1, 4):
                return number
        except ValueError:
            pass


def generate_integer(number):
    questions_list = 0
    score = 0
    while questions_list < 10:
        if number == 1:
            num1 = random.randint(0, 10)
            num2 = random.randint(0, 10)
        elif number == 2:
            num1 = random.randint(10, 100)
            num2 = random.randint(10, 100)
        else:
            num1 = random.randint(100, 1000)
            num2 = random.randint(100, 1000)
        questions = int(input(f"{num1} + {num2} = "))
        if questions == num1 + num2:
            pass
            score += 1
        else:
            for n in range(1, 3):  # checks the number of tries is below 3
                print("EEE")
                questions = int(input(f"{num1} + {num2} = "))
                n += 1
                if questions != num1 + num2:
                    pass
                else:
                    continue
            print(f"{num1} + {num2} = {num1+num2}")
        questions_list += 1
    print(f"Score: {score}")


if __name__ == "__main__":
    main()
