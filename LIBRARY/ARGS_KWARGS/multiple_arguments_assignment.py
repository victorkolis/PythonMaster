evens = range(0, 10, 2)

# 01 - Unpacking
zero, one, *numbers = evens

print(f'{zero}\n{one}\n{numbers}')

# 02 - Unpacking an entire list
print(*evens)


# 03 - Unpacking an entire list with separator
print(*evens, sep='-')
