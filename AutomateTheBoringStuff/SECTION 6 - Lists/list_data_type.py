# list_data_type.py

spam = ['A', 'B', 'C', 'D', 'E']

list_of_list = [['A', 'B', 'C', 'D', 'E'], ['1', '2', '3', '4', '5', '6']]

# accessing by index

print(spam[2])
print(list_of_list[1][4])

# slicing - up to but not including
print(spam[1:4])

# sublist - slice it up to the last element in the list
print(spam[2:])
print(spam[:2])

# chaging item in a list
print(spam)

spam[0] = 'Z'
print(spam)

# delete an element from a list
del spam[3]
print(spam)

# get the size of a list
len(spam)

# list concatenation
print(spam + list_of_list)