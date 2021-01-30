#!/usr/bin/env python3

# Insert allows you to add an element to an array at a given/specific position

a = [1, 1]

a.insert(1, 2)
print(a)

# Adding elements to the center of the array/list
a.insert(len(a)//2, 2)
print(a)

a.insert(len(a)//2, 3)
print(a)

# Adding elements to the end
a.insert(len(a), (88, 89))
print(a)

# Adding elements to the beginning of the array/list
a.insert(0, -10)
print(a)
