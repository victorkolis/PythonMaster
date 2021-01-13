# Intersections 01

odds = {1, 3, 5, 7}
numbers = {1, 2, 4, 5, 6, 7, 8}

# Reading: numbers.remove_from_me_all_that_is_in(odds)
evens = numbers.difference(odds)
print(evens)

# Uniting 2 sets
all_numbers = odds.union(numbers)
print(all_numbers)

# Intersections 02
art_students = {'Ana', 'Lucy', 'Sheila', 'Ellen'}
math_students = {'Ana', 'Zoe', 'Amanda', 'Ellen'}

both = art_students.intersection(math_students)
print(both)
