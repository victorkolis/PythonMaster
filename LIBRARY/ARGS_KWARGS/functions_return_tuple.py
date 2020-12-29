def tuple_returner(*args):
    return args, args[1]  # It is possible to access indexes like a list
    

print(tuple_returner(1, 2, 3, 4, 5))
