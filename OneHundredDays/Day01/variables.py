# This software objective is to show how variables operate(in a very basic way) and show how they facilitate/are necessary for the programming process

#01 - simple use of a variable to store the input collected from user input
name = input("What is your name? ")
print(name)

#02 - breaking the code down into pieces facilitates the readability
name = input("What is your name? ")
length = len(name)
print(name + ", the length of your name is: " + str(length))
