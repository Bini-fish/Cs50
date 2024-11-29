def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
    print(
        num_between_letters(plate),
        is_letter(plate),
        start_with_two_L(plate),
        max_length(plate),
        has_punctuation(plate),
    )


def is_valid(plate):
    i = 0
    while i < len(plate):
        if plate[i].isalpha() == False:
            if plate[i] == "0":
                return False
            else:
                break
        i += 1
    if len(plate) < 2 or len(plate) > 6:
        return False
    j = 0

    # check no number is between letters
    for j in range(0, len(plate)):
        if plate[j] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            if plate[-1].isalpha() == False:
                return True
            else:
                return False
        j += 1
    if plate[0].isalpha() == False or plate[1].isalpha() == False:
        return False

    for p in plate:
        if p in [".", ",", "!", " "]:
            return False

    return True


# numbers can't come in the middle, they must come at the end

# is_letter(plate)
# max_length(plate)
# start_with_two_L(plate)
# num_between_letters(plate)
# has_punctuation(plate)


def is_letter(plate):
    i = 0
    while i < len(plate):
        if plate[i].isalpha() == False:
            if plate[i] == "0":
                return False
            else:
                break
        i += 1


# contain max of 6 characters
def max_length(plate):
    if len(plate) < 2 or len(plate) > 6:
        return False


# start with at least two letters


def start_with_two_L(plate):
    if plate[0].isalpha() == False and plate[1].isalpha() == False:
        return False

    # check no number is between letters


def num_between_letters(plate):
    for j in range(0, len(plate)):
        if plate[j] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            if plate[len(plate) - 1].isalpha() == True:
                return True
        else:
            return False
        j += 1


# no .,! or space punctuations
def has_punctuation(plate):
    for p in plate:
        if p in [".", ",", "!", " "]:
            return False


if __name__ == "__main__":
    main()

# completed
