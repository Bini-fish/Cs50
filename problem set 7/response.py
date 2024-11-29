import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = r"^https?://www\.youtube\.com/embed/(?P<url_name>.+)"
    match = re.search(pattern, s)
    url = match.group("url_name")
    output = f"https://youtu.be/{url}"
    return output




if __name__ == "__main__":
    main()
