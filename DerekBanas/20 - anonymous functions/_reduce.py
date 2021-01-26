# reduce receives a list and returns only one value

from functools import reduce

print(reduce((lambda x, y: x + y), range(1, 7)))  # Similar to print(1 + 2 + 3 + 4 + 5 + 6)
