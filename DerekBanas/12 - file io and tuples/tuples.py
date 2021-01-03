# Common operations

my_tuple = tuple([x for x in range(2, 11, 2)])
print('First value of my tuple: {}'.format(my_tuple[0]))
print(my_tuple[0:3])
print('Length of my_tuple:', len(my_tuple))
print('34 in my_tuple:', 34 in my_tuple)

my_list = list(my_tuple)
print(my_list)

items = [1, 2, 4]
my_items = tuple(items)
print(my_items)
