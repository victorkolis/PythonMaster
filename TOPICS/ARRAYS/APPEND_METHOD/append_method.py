#!/usr/bin/env python3

a = [1, 2]
b = []
c = [lambda x: x * 2, lambda y, z: y+z]

# Appending to a list

a += [1]  # a.append(1)
b.append('A')
c[len(c):] = [lambda a: a - a ** 2]


print(f'{a} {b} {c}')
