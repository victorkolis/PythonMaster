# if_elif_else

password = input("Enter the password: ")

if password == "swordfish":
    print("Access granted...")
else:
    print("Access denied...")

# if, elif, else

age = int(input("How old are you?\n"))

if age == 0 or age < 4:
    print("I did not know babies could talk.")
elif age < 0:
    print("So... you are Benjamin Buttom.")
elif age >= 4 and age < 11:
    print("Ah, you are just a kiddo!")
elif age >= 11 and age < 18:
    print("Wow! You are a teenager already!")
elif age >= 18 and age < 40:
    print("Adults are the brains and muscles of a society.")
elif age >= 40 and age < 90:
    print("Nice age to be at.")
elif age >= 90 and age < 120:
    print("Wow! You are a legend!")
else:
    print("Get out of here!!!")