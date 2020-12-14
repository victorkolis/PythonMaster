import random

random_number = random.randrange(1, 51)
i = 1

while i != random_number:
    i += 1
    print(i)
print("The random value is: ", random_number)
