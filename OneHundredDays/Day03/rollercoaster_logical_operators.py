# Nested if statement

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print(f"Child tickets are ${bill}.00")
    elif age <= 18:
        bill = 7
        print(f"Youth tickets are ${bill}.00")
    elif 45 <= age <= 55:
        bill = 0
        print(f"Youth tickets are ${bill}.00")
    else:
        bill = 12
        print(f"Adult tickets are ${bill}.00")
    
    wanna_a_pic = input("Do you want a ride picture, +$3.00, (y|n)? ")
    wanna_a_pic = wanna_a_pic.upper()
    
    if bill == 0:
        print(f"The bill total is ${bill}")
    elif wanna_a_pic == "Y":
        bill += 3
        print(f"The bill total is ${bill}")
    else:
        print(f"The bill total is ${bill}")    
else:
    print("You cannot ride!")
