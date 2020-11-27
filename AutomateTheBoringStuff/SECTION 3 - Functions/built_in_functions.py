# built_in_functions.py

# There are two ways of importing a module/built-in function

# random
import random, sys


# from random import * -> not so good for readability

rand_number = random.randint(1, 10)
print(rand_number)

# sys

sys.exit()

print("This never executes")
