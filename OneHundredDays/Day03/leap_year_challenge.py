# This software objective is to figure out whether the year is a leap one or not

year = int(input("Which year do you want to check? "))

if year % 4 == 0 and year % 100 != 0:
    print(f"{year} is a leap year!")
elif year % 400 == 0:
        print(f"{year} is a leap year!")
else:
    print(f"{year} is not a leap year!")