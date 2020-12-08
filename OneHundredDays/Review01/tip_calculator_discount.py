# This software objective is to calculate the tip and split the bill into however many people were involved in
# If the price is ended in 7, say $57.00 or $50.07 or above $300.00 there is a 3% discount, however the tip is not added to this discount.

import subprocess

def tip_calculator():
    suprocess.call('clear')
    print('Welcome to the tip calculator.')
    bill_total = int(input('The bill total is: $'))
    if bill_total > 300 or str(bill_total).endswith('7'):
        bill_total -= bill_total * 0.03
    
    correct_value = False
    while not correct_value:
        tip = int(input('Enter the tip. (10% - 12% - 15%): '))
        if tip == 15 or tip == 12 or tip == 10:
            correct_value = True
    bill_total += bill_total * (tip / 100)
    amount_of_people_paying = int(input('How many people are going to pay? '))
    bill_total /= amount_of_people_paying
    print(f'Each person is going to pay ${round(bill_total, 2)}')

tip_calculator()
