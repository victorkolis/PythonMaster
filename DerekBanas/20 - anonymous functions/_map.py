one_to_10 = range(1, 11)
def dbl_num(num):
    return num * 2

# list(map(function, value)) => make a list of a mapped out function using the following values (understandability)
print(list(map(dbl_num, one_to_10)))
print(list(map((lambda x: x * 17), one_to_10)))

a_list = list(map((lambda x, y: x + y), [1, 2, 3], [1, 2, 3]))
print(a_list)
