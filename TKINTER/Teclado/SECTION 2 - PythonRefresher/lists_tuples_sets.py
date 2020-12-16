# Lists can be modified in place
lists = [1, 3, 5, 1]

# Tuples cannot be modified
tuples = (1, 3, 5, 1)

# Sets do not contain duplicates and does not keep a specific order
sets = {1, 3, 5, 1}

print(lists)
print(tuples)
print(sets)

# Accessing elements through subscript notation
print(lists[0])
print(tuples[0])

# set object is not subscriptable
# print(sets[0]) this would generate e TypeError

# Modifying elements
lists[0] = 233
print(lists[0])
print(lists)

# Appending elements to a list(adding to the end of it)
lists.append(777)
lists += [999]
print(lists)

# Removing elements from a list
lists.remove(233)
print(lists)

# add() method to add to a set, since it does not have a definite end
sets.add(0.009)
print(sets)
