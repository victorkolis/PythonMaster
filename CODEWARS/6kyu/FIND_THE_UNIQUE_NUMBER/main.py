def find_unique(arr):
    # Fastest way I found
    number_counter = list(set(arr))
    for number in number_counter:
        if arr.count(number) < 2:
            return number
        else:
            return number_counter[1]


print(find_unique([1, 0, 1, 1]))
