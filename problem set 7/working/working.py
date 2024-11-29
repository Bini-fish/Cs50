import re

def main():

    print(convert(input("Hours: ")))

def convert(s):
    time_table = {
    "1PM":"13",
    "2PM":"14",
    "3PM":"15",
    "4PM":"16",
    "5PM":"17",
    "6PM":"18",
    "7PM":"19",
    "8PM":"20",
    "9PM":"21",
    "10PM":"22",
    "11PM":"23",
    "12PM":"12"}
    #pattern = r"(?P<hour>\d\d?)(?P<minute>\:\d\d)?(?P<time>AM|PM)"
    if match := re.search(r"((?P<hour>^[1-9]|1[0-2]):?(?P<minute>(0[0-9])?|([0-5][0-9])?) (?P<time>AM|PM)) "
                          r"to ((?P<hour2>[1-9]|1[0-2]):?(?P<minute2>(0[0-9])?|([0-5][0-9])?) (?P<time2>AM|PM))$", s):
                          hour = match.group("hour")
                          minute = match.group("minute")
                          time = match.group("time")
                          hour2 = match.group("hour2")
                          minute2 = match.group("minute2")
                          time2 = match.group("time2")
                          final_time = ""


                          if hour == "12" and "AM" in time:
                            final_time += "00"
                            pass
                          elif len(hour) == 1 and "AM" in time:
                            final_time += "0"+hour
                          elif "AM" in time:
                            final_time += hour
                          elif "PM" in time:
                            final_time += time_table.get(hour+"PM")


                          else:
                            final_time += hour
                          if minute:
                            final_time += ":"+minute
                          else:
                            final_time += ":00"
                            # for the second section
                          final_time += " to "
                          if hour2 == "12" and "AM" in time2:
                            final_time += "00"
                          elif "AM" in time2:
                            final_time += hour2
                          elif "PM" in time2:
                            final_time += time_table.get(hour2+"PM")
                          else:
                            if len(hour2) == 1:
                                final_time += "0"+hour2
                            else:
                                final_time += hour2
                          if minute2:
                            final_time += ":"+minute2
                          else:
                            final_time += ":00"


                          return final_time

    else:
        raise ValueError


if __name__ == "__main__":
    main()



'''
print(match)
    initial = match[0][0] + match[0][2]
    print(initial)
    initial_minute = match[0][1]
    final_minute = match[1][1]
    final = match[1][0] + match[1][2]

    if initial_minute:
        if int(initial_minute.strip(":")) > 59:
            raise ValueError
        start = time_table[initial].strip()+initial_minute
    else:
        start = time_table[initial].strip()+":00"
    if final_minute:
        if int(final_minute.strip(":")) > 59:
            raise ValueError
        end = time_table[final].strip()+final_minute
    else:
        end = time_table[final].strip()+":00"
    final_match = f"{start} to {end}"
    return final_match

'''
