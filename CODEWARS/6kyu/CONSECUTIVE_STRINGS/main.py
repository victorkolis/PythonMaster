def longest_consecutive(string_arr, k):
    array_length = len(string_arr)
    consecutive_list = []
    if array_length == 0 or array_length < k or k <= 0:
        return ''
    else:
        for string_arr_index in range(array_length):
            new_word = ''
            for adder in range(k):
                try:
                    new_word += string_arr[string_arr_index + adder]
                except IndexError:
                    pass

            consecutive_list += [new_word]

    longest_consecutive_string = ''
    for index, word in enumerate(consecutive_list):
        if len(consecutive_list[index]) > len(longest_consecutive_string):
            longest_consecutive_string = consecutive_list[index]

    return longest_consecutive_string


print(longest_consecutive(["zone", "abigail", "theta", "form", "libe", "zas"], 2))
