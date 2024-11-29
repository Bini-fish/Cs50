fruits_dict = {}
while True:
    # loop the input until EOFError (ctrl+d is hit)
    try:
        # prompt the user for input (case insensitive)
        fruits = input().upper() # all caps(.upper())
        if fruits not in fruits_dict:
            fruits_dict[fruits] = 1
        elif fruits in fruits_dict:
            fruits_dict[fruits] += 1
        else:
            pass
    except KeyError:
        # handle KeyError (when there is no input)
        pass
    except EOFError:
        sorted_fruits_dict = dict(sorted(fruits_dict.items()))
        for key, value in sorted_fruits_dict.items():
                print(value,key) #prefix each line with the number of times the item repeated.
        break


# output in

    # sorted alphabetically (sorted())

