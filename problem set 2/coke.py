AmountDue = 50


accepted_values = [5, 10, 25]
# checking if the Amount due is less than 0
while AmountDue > 0:
    # checking if the Amount due is less than 0
    print(f"Amount Due: {AmountDue}")
    # prompting the user to enter a coin
    coin = int(input("Insert Coin: "))
    # checking if the user entered 5,10,or 25
    if coin in accepted_values:
        # subtracting the amount due to our coin entered
        AmountDue -= coin
    # printing change owed when we finish paying our debt
print(f"Change Owed: {abs(AmountDue)}")
