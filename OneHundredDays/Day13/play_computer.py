# play_computer.py

# The year 1994 is never checked neither is 1980
year = int(input("What's your year of birth: "))
if year > 1980 and year < 1994:
    print("You are a millenial.")
elif year > 1994:
    print("You are a Gen Z.")

# The year 1994 and 1980 are now checked
year = int(input("What's your year of birth: "))
if year >= 1980 and year <= 1994:
    print("You are a millenial.")
elif year > 1994:
    print("You are a Gen Z.")
