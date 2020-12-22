# Lists

# One data type is the best way to go
numbers = [0, 1, 2, 3]

# Mixing data types is not the most recommended way to go
mixed_list = [9, 'Battery', 'MONDAY', 15.7]

# Creating a number list
one_to_ten = list(range(11))
print(one_to_ten)

# Combining lists
mixed_list += numbers
print(mixed_list)

# Using index to retrieve info
print(mixed_list[2])

# Getting a list length
print('The length of numbers list is', len(numbers))


# Slicing a list
first_3 = mixed_list[0:3]
print(first_3)

for item in first_3:
    print('{} : {}'.format(first_3.index(item), item))

# Using a value to find its index
day_of_the_week = mixed_list.index('MONDAY')
print(day_of_the_week)

# Finding how many times an item occur in a list
repeated_list = [1, 1, 4, 5, 6, 7, 8, 9, 10]
print(repeated_list.count(1))

# Replacing item via index
repeated_list[1] = 2
print(repeated_list)


# Appending/Adding to the end of a list
repeated_list += [0]
repeated_list.append(3)
print(repeated_list)

# Organizing a list
repeated_list.sort()
print(repeated_list)

