import math

# Creating a list from a range
odd_list = [number for number in range(1, 15, 2)]
print(odd_list)

for number in odd_list:
    print(number, end=', ')
print()

num_list = [1, 2, 3, 4, 5]
list_of_functions = [[round(math.pow(m, 2)), round(math.pow(m, 3)), round(math.pow(m, 4)),
                      round(math.pow(m, 5))] for m in num_list]

for number in list_of_functions:
    print(number)
