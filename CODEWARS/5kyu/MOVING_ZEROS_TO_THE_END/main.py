def move_zeros(array):
    new_array = []
    zeros_found = 0
    for element in array:
        if element is False:
            new_array += [element]

        elif element != 0 or element != 0.0:
            new_array += [element]

        else:
            zeros_found += 1

    for _ in range(zeros_found):
        new_array += [0]

    return new_array


print(move_zeros([1, 0, False, 0, 1, 1]))
