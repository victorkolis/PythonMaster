def simple_parity(string):
    string = string.upper()
    new_string = ''
    if len(string) % 2 != 0:
        return 'IMPAR'
    elif len(string) == 2:
        new_string = list(string)
        new_string[0], new_string[1] = new_string[1], new_string[0]
        new_string = ''.join(new_string)
    else:
        for index in range(len(string) // 2):
            new_string += string[index] + string[::-1][index]

    return new_string


print(simple_parity('ABCDEFGHIJKLMN'))
