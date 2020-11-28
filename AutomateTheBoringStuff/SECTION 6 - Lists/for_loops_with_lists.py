# for_loops_with_lists.py

# A range is a list like object - but technically they are called sequences in python

for i in range(4):
    print(i)

print("***************\n\n")

for i in [0, 1, 2, 3]:
    print(i)

print("***************\n\n")

# This returns/ creates a list out of the range object
print(list(range(4)))

# Using the list length to loop
supplies = ['pens', 'staplers', 'flame-throwers', 'binders']

for i in range(len(supplies)):
    print(f"The index {i} in supplies is: {supplies[i]}")

# Multiple assignment
cat = ['fat', 'orange', 'loud']
print(cat)
size, color, disposition = cat
print(f"size: {size}\ncolor: {color}\ndisposition: {disposition}")

a = 5
b = 'F'

a, b = b, a
print(f"a: {a}\nb: {b}")

# Augmented assignment operators

b += 5
print(b)
