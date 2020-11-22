# This software objective is to find out love compatibility

print("Welcome to the love calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()
names_concatenated = name1 + name2

true = names_concatenated.count("t") + names_concatenated.count("r") + names_concatenated.count("u") + names_concatenated.count("e")
love = names_concatenated.count("l") + names_concatenated.count("o") + names_concatenated.count("v") + names_concatenated.count("e")

score = str(true) + str(love)

score = int(score)

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 or score >= 50:
    print(f"Your score is {score}, ❤️️ you are alright together. ❤️️")
else:
    print(f"Your score is {score}, you go together like coke and mentos.")
