# Randomization

import random

random_integer = random.randint(1, 5)
print(random_integer)

random_float = random.random()
print(random_float)

print(round(random_float, 2) * random_integer)