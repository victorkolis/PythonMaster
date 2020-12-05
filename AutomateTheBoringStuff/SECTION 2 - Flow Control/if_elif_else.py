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
elif 4 <= age < 11:
    print("Ah, you are just a kiddo!")
elif 11 <= age < 18:
    print("Wow! You are a teenager already!")
elif 18 <= age < 40:
    print("Adults are the brains and muscles of a society.")
elif 40 <= age < 90:
    print("Nice age to be at.")
elif 90 <= age < 120:
    print("Wow! You are a legend!")
else:
    print("Get out of here!!!")