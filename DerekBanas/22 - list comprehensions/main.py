#!/usr/bin/env python3


# Using map and list comprehension to get the same effects
print(list(map(lambda x: x * x + x, range(100))))
print([x * x + x for x in range(100)])

# Using filter and list comprehension to get the same effects
print(list(filter(lambda x: x % 2 != 0, range(1, 11))))
print([x for x in range(1, 11) if x % 2 != 0])


# To the power
print([x ** 2 for x in range(50) if x % 5 == 0])

# Two values
print([x - y for x in range(1, 3) for y in range(7)])

# List comprehension in list comprehensions
print([x for x in [y * 3 for y in range(3000)]])
