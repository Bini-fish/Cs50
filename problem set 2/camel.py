string = input("camelCase: ")


def camel_case_split(s):
    result = []
    start = 0
    for i, c in enumerate(s[1:], 1):
        if c.isupper():
            result.append(s[start:i])
            start = i
    result.append(s[start:])
    return "_".join(result).lower()


print(f"snake_case: {camel_case_split(string)}")
