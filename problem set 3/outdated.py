import re


def main():
    date = input("Date: ")
    print(dates(date))


def dates(date):
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    split = re.split(r"/|\,|\s+", date)
    for x in range(len(split) - 1):
        if split[x] == "":
            del split[x]
        x += 1
    for i in range(11):
        if split[0] == months[i]:
            split[0] = i + 1
            break
        i += 1

    # MM/DD/YYYY -> YYYY/MM/DD
    try:
        day = int(split[1])
        month = int(split[0])
        year = int(split[2])
        if day > 31:
            pass
        elif month > 12:
            pass
        else:
            return f"{year}-{month:02}-{day:02}"
    except ValueError:
        pass


if __name__ == "__main__":
    main()
