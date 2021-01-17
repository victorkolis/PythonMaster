def parse(data):
    value = 0
    number_list = []
    for command in data:
        if command == 'i':
            value += 1
        elif command == 'd':
            value -= 1
        elif command == 's':
            value *= value
        elif command == 'o':
            number_list += [value]

    return number_list


print(parse('iiisdoso'))
