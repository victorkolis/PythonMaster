def sum_strings(string_1, string_2):
    if string_1 == '':
        string_1 = 0

    if string_2 == '':
        string_2 = 0

    string_1 = int(string_1)
    string_2 = int(string_2)
    return str(string_1 + string_2)


print(sum_strings('0', '7'))
