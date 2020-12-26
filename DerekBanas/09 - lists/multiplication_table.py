numbers = range(1, 11)

for index in range(len(numbers)):
    if index == 9:
        break
    else:
        multiplication_table = [[number * numbers[index] for number in numbers]]
        for number in multiplication_table:
            print(number)
