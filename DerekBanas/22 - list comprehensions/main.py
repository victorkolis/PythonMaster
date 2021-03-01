#!/usr/bin/env python3


# Using map and list comprehension to get the same effects
print(list(map(lambda x: x * x + x, range(100))))
print([x * x + x for x in range(100)])

# Using filter and list comprehension to get the same effects
print(list(filter(lambda x: x % 2 != 0, range(1, 11))))
print([])