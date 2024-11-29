def main():
    character = input("Input: ")
    print(voweless(character))


def voweless(character):
    vowels = ["a", "e", "i", "o", "u"]
    vowel_less = ""
    for c in character:
        if c.lower() in vowels:
            continue
        vowel_less += c
    return vowel_less


if __name__ == "__main__":
    main()
