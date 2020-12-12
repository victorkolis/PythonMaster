for i in [2, 4, 6, 8, 10]:
    print('i =', i)

print(range(10))

""" 
A range object returns a list of numbers ranging from
a start point up to but not including the end point
"""

# Creating a list of numbers from a range() object
numbers = list(range(10))
print(numbers)

# Combining for and range
# 1.
print('\nFirst method: ')
for number in range(5):
    print(f'number = {number}')

# 2.
print('\nSecond method: ')
for number in range(2, 5):
    print(f'number = {number}')

# 3.
print('\nThird method: ')
for number in range(2, 10, 2):
    print(f'number = {number}')
