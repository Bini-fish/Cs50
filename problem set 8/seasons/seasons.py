import sys
import inflect
import re
from datetime import date

p = inflect.engine()

def main():
    # takes birthdate and returns the minutes till today rounded to the nearest intiger
    birth_date = input("Date of Birth: ")
    print(birthdate_minutes(birth_date))

def birthdate_minutes(bday):
    today = date.today()
    pattern = r"(?P<year>^1\d{3}|20[0-2][0-4])-(?P<month>0?[1-9]|1[0-2])-(?P<day>0?[1-9]|1[0-9]|2[0-9]|30)$"
    match = re.search(pattern, bday)
    if match:

        year = int(match.group("year"))
        month = int(match.group("month"))
        day = int(match.group("day"))

        bday = date(year,month,day)

        difference = (today - bday).days
        age_in_minutes = int(difference) * 1440

        to_word = p.number_to_words(age_in_minutes, andword="")+" minutes"
        return (to_word).capitalize()
    else:
        sys.exit("Invalid date")

if __name__ == "__main__":
    main()
