# password_generator_challenge.py

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']



print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []
final_password = ""

# Get the letters into the password list
for i in range(0, nr_letters):
    random_index = random.randint(0, len(letters) - 1)
    password.insert(i, letters[random_index])

# Get the symbols into the password list
for i in range(0, nr_symbols):
    random_index = random.randint(0, len(symbols) - 1)
    password.insert(i, symbols[random_index])

# Get the numbers into the password list
for i in range(0, nr_numbers):
    random_index = random.randint(0, len(numbers) - 1)
    password.insert(i, numbers[random_index])

# Last suffle because the other three for loops kind of generated an ordered type of password
random.shuffle(password)
password = ''.join(password)

print(password)