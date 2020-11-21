# This software objective is to calculate the tip and split the bill into however many people were involved in

print("Welcome to the tip calculator")
bill_total = int(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10%, 12% or 15%? "))
tip_percentage /= 100
bill_total += bill_total * tip_percentage
how_many_people = int(input("How many people to split the bill? "))
bill_total /= how_many_people
print(f"Each person should pay: ${bill_total}")