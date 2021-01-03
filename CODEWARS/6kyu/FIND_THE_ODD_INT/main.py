def find_odd(number_list):

    for number in number_list:
        count = number_list.count(number)
        if not count % 2 == 0:
            odd_found = number
    return odd_found


print(find_odd([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]))
