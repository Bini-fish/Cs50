def main():
    c = fuel()
    if c < 0.99 and c > 0.1:
        d = c * 100
        print(f"{round(d)}%")
    elif c > 1:
        pass
    else:
        pass


def fuel():
    while True:
        try:
            fraction = input("Fraction: ")
            numbers = fraction.split("/")
            a = int(numbers[0])
            b = int(numbers[1])
            c = a / b
        except (ValueError, ZeroDivisionError):
            pass
        else:
            if c >= 0.99:
                print("F")
            elif c <= 0.1:
                print("E")
            elif c > 1:
                pass
            return c


if __name__ == "__main__":
    main()
