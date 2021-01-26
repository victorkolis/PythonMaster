def array_diff(a, b):
    for element in b:
        while True:
            if element in a:
                a.remove(element)
            else:
                break
    return a


print(array_diff([1, 2, 2, 2, 3, 4], [2, 4]))
