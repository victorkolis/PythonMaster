def calc(x):
    total1 = ''

    for index, word in enumerate(x):
        total1 += str(ord(word))

    total2 = total1.replace('7', '1')

    return sum(map(int, total1)) - sum(map(int, total2))


print(calc('abcdef'))
