# Generate a random list of five numbers between 1-9

import random

random_list = []
for number in range(5):
    random_list += [random.randrange(1, 9)]
random_list.sort()
print(random_list)
