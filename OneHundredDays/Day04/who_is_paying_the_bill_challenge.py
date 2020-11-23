# This software objective is to simulate a Russian Roulette but with bills

import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

namesAsCSV = input("Give me everybody's names, separated by comma: ")
names = namesAsCSV.split(", ")

random_person = random.randint(0, len(names) - 1)

print(f"{names[random_person]} is going to pay the bill.")