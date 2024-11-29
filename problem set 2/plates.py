def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


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
    if plate[0].isalpha() == False or plate[1].isalpha() == False:
        return False


# no .,! or space punctuations
def has_punctuation(plate):
    for p in plate:
        if p in [".", ",", "!", " "]:
            return False


main()

# completed
