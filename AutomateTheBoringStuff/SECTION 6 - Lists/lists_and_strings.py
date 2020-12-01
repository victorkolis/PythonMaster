# list_and_strings.py

import copy

# Make a string a list
print(list('Hello'))

# Index
_list = ['python list']
string = 'python'

# For loop in a string
for letter in string:
    print(f'{letter}', end=' ')

print('\n')
# For loop in a list
for index in range(len(_list)):
        _list = list(_list[index])
        print(_list)

# Lists use memory reference
vowels = ['A', 'E', 'I', 'O', 'U']
letters = vowels

print(vowels)
print(letters)

letters[3] = 'F'

print(vowels)
print(letters)

# In order to copy the real/raw value of a list use copy.deepcopy(list)
spam = ['A', 'B', 'C']
eggs = copy.deepcopy(spam)
eggs[1] = 2

print(spam, eggs)
