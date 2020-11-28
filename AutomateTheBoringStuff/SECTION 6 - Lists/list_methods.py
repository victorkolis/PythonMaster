# list_methods.py

# index
greeting = ['hey', 'howdy', 'hello', 'hi', 'heyas']
print(greeting.index('heyas'))

# append
animals = ['eagle', 'lion', 'ox', 'snake']
animals.append('Moose')
print(animals)

# insert
animals.insert(1, 'chicken')
print(animals)

# remove - deletes by argument/value (only the first instance it finds)
animals.remove('snake')
print(animals)

# delete - deletes by index/position in the array
del animals[4]
print(animals)

# sort - rearranges the elements in a list (alphabetial/numerical order)
'''
sort does not use alphabetical but ASCII-betical order which is the exact same
thing except it priorizes the capital letters first so:

"AB" would come before "aa" in a sort(). Which means, a capital "Z" comes before
a lower-case "a".

'''

animals.sort()
print(animals)

# sort(reverse=True)
animals.sort(reverse=True)
print(animals)

# whenever there is numbers and strings the sort raises an error

# Breaking the ASCII-betical order

# ASCII-betical
name_list = ['ana', 'Zedon', 'Seryah', 'sheila', 'Victor']
name_list.sort()
print(name_list)

# non-ASCII-betical
name_list.sort(key=str.lower)
print(name_list)
