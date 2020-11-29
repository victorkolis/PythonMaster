# auction_bid.py

# This code is OS based so line # must be changed according

import subprocess
subprocess.call("clear")

import art

print(art.logo)
print("Welcome to the secret auction program.")


isTheAnyBidderLeft = 'yes'

winner = 0


while isTheAnyBidderLeft == 'yes':
    name = input("What is your name?\n")
    bid = float(input("What is your bid?\n$"))
    bidders = {}
    bidders[name] = bid
    isTheAnyBidderLeft = input("Is there any other bidder? Type 'yes' or 'no': ")
    if isTheAnyBidderLeft == 'yes':
        subprocess.call("clear")
        print(bidders)
    
    else:
        for name in bidders:
            if bidders[name] > winner:
                winner = {name: bidders[name]}
        for key in winner:
            winner_name = key
            winner_bid = winner[key]
            print(f"The winner is {winner_name} with a bid if ${winner_bid}.")

