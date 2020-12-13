value = 0

while value <= 20:
    if(value % 2) == 0:
        value += 1
        continue
    if value == 15:
        break
    print(f'Odd: {value}')
    value += 1
