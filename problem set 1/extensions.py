name = input("File name: ").lower().strip()
splitted = name.split(".")
length = len(splitted)
extension = splitted[length - 1]
first_word = splitted[0]

if extension == "gif" or extension == "jpeg" or extension == "png":
    print(f"image/{extension}")
elif extension == "jpg":
    print(f"image/jpeg")
elif extension == "pdf" or extension == "zip":
    print(f"application/{extension}")
elif extension == "txt":
    print(f"text/{first_word}")
else:
    print("application/octet-stream")
