# This software objective is to simulate a Russian Roulette but with bills

import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

namesAsCSV = input("Give me everybody's names, separated by comma: ")
names = namesAsCSV.split(", ")

# random.choice() picks a random item from a list
random_person = random.choice(names)

print(f"{random_person} is going to pay the bill.")