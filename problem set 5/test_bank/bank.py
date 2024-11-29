
def main():
    answer = input("Greeting: ").strip().lower()
    bank(answer)


def bank(answer):
    first_word = answer.split(",")[0]
    if first_word == "hello":
        print("$0")
    elif answer[0] == "h" and first_word != "hello":
        print("$20")
    else:
        print("$100")

if __name__ == "__main__":
    main()
