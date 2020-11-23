# This software objective is to simulate a coin toss

import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

random_side = random.randint(0, 1)
 
if random_side == 1:
    print("Heads")
else: 
    print("Tails")
