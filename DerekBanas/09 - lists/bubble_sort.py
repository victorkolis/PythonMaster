
number_list = [6, 7, 2, 1, 0, 3, 4, 12, 20, 21, 45, -4, -13]

is_sorted = False
while not is_sorted:
    is_sorted = True
    for index in range(len(number_list) - 1):
        if number_list[index] > number_list[index + 1]:
            is_sorted = False
            number_list[index], number_list[index + 1] = number_list[index + 1], number_list[index]

print(number_list)
