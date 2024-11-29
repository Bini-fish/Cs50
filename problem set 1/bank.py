answer = input("Greeting: ").strip().lower()
first_word = answer.split(",")[0]
if first_word == "hello":
    print("$0")
elif answer[0] == "h" and first_word != "hello":
    print("$20")
else:
    print("$100")