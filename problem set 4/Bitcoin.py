# A program that prompts the user for the amount of bitcoin the user wants and returns the updated price of the coin
import requests
import json
import sys

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
read_response = response.json() # formats the response in JSON form enabling us to edit it more effectively
current_price_str = read_response["bpi"]["USD"]["rate"] # retriving the current price
current_price = current_price_str.split(',') # splitting the current price using a comma
current_price = float("".join(current_price)) #joining and converting it to a string
try:
    if len(sys.argv) != 2: # if the user didn't enter an argument other than
        print("Missing command-line argument")
        sys.exit()
    final_price = float(sys.argv[1]) * current_price
    print(f'${final_price:,.4f}'.format(final_price))
except ValueError:
    print("Command-line argument is not a number")
    sys.exit()
except requests.RequestException:
    print("Command-line argument is not a number")
    sys.exit()


