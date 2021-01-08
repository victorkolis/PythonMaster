def even_binary(n):
    print(n)
    n = n.split()
    binary = {'110': 6, '100': 4, '010': 2, '000': 0}  # This dictionary brings clarity and it is also used in the code
    positions = {}
    binary_list = []
    for index in range(len(n)):
        if n[index] in binary:
            positions[index] = n[index]
            binary_list += [n[index]]

    binary_list.sort()
    index = 0
    for value in positions.keys():
        n[value] = binary_list[index]
        index += 1

    n = ' '.join(n)
    return n


print(even_binary("101 100 010 101 010"))


# My favorite Kata
