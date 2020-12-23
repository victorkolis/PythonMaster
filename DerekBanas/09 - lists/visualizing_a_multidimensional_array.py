array = [[0] * 10 for _ in range(10)]

for row in range(4):
    for column in range(4):
        array[row][column] = "{} : {}".format(row, column)

for row in range(4):
    for column in range(4):
        print(array[row][column], end=' || ')
    print()
