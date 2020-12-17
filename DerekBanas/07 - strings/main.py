import string

text = 'My sentence inside the text variable'
print(f'The \'text\' variable size is {len(text)}')

# Index
print(f'text[13] = ', text[13])

# Substrings
print(text[0:4])
print(text[8])
print(text[-1])

# Reversing strings
print('Reverse', text[::-1])

# Repeat string
print('Hello ' * 5)

# Concatenating strings
print('Victor' + 'Kolis')

# Printing a given amount of the text
for _ in range(len(text) - round(len(text) / 2)):
    print(_)

# Printing every character in a string
for letter in text:
    print(letter)
