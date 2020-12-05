# dictionary.py

# Key - Value

# Strings
synonyms = {'Work': 'Labour', 'Study': 'Learn', 'Speak': 'Talk', 'Look for': 'Search'}
try:
    print(synonyms[input('What\'s the synonym of: ').title()])
except KeyError:
    print('Error!')

# Get the key by the 'in'
if 'Speak' in synonyms:
    print('Speak' in synonyms)

# list() is used in order to get the return without their prefixes
# keys() - returns the keys
print(list(synonyms.keys()))

# values() returns the values
print(list(synonyms.values()))

# items() - returns a tuple of the key and value
print(list(synonyms.items()))

print('')  # just a break

# Looping through keys and values
for key in synonyms.keys():
    print(key, end=', ')

print('')  # just a break

for value in synonyms.values():
    print(value, end=', ')

print('')  # just a break
# Multiple assignment for loop
for key, value in synonyms.items():
    print(f'{key} - {value}', end=', ')

print('')  # just a break

# Get method
key_search = synonyms.get('Labour', 'Nothing found!')
print(key_search)

# Setdefault - if a a key already exists it won't overwrite it and it will return what it has/what is already attributed to that key
print(synonyms.setdefault('Understand', 'Comprehend'))
print(synonyms.setdefault('Work', 'Wrought'))
