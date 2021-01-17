def find_difference(a: list, b: list) -> int:
    a_volume = 1
    b_volume = 1
    for number in a:
        a_volume *= number
    for number in b:
        b_volume *= number

    return abs(a_volume - b_volume)


print(find_difference([3, 2, 5], [1, 4, 4]))
