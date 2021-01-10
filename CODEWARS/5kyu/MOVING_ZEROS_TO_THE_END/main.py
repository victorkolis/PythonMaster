def move_zeros(array):
    new_array = []
    counter = 0
    for element in array:
        if element is False:
            new_array += [element]

        elif element != 0 or element != 0.0:
            new_array += [element]

        else:
            counter += 1

    for _ in range(counter):
        new_array += [0]

    return new_array


print(move_zeros([1, 0, False, 0, 1, 1]))
