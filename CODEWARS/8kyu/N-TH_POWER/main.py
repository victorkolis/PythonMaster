def index(array, n):
    return -1 if n >= len(array) else array[n] ** n


print(index([1, 2, 3, 4], 2))
