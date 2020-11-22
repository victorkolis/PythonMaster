# This software objective is for a user to order pizza

print("Welcome to Python Pizza Deliveries!")
size = input("What pizza size do you want, S, M or L? ")
size = size.upper()

add_pepperoni = input("Do you want pepperoni, (y|n)? ")
add_pepperoni = add_pepperoni.upper()

extra_cheese = input("Do you want extra cheese, (y|n)? ")
extra_cheese = extra_cheese.upper()


total = 0

if size == "S":
    total = 15
    if add_pepperoni == "Y":
        total += 2
    if extra_cheese == "Y":
        total += 3
    print(f"Total {total}.00")
elif size == "M":
    total = 20
    if add_pepperoni == "Y":
        total += 2
    if extra_cheese == "Y":
        total += 3
    print(f"Total {total}.00")
elif size == "L":
    total = 25
    if add_pepperoni == "Y":
        total += 2
    if extra_cheese == "Y":
        total += 3
    print(f"Total {total}.00")
else:
    print("Error: 51 - Ivalid request!")
    print("Have an nice day!")
