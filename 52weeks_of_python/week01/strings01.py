# Strings are the most magical bit-beings
print('This is a string')

# Messing around with strings
each_word = 'This is a string'.split()
print(each_word)

each_letter = list('Each letter')
print(each_letter)

# Transforming strings
each_letter_uppercased = list('Each letter'.upper())
print(each_letter_uppercased)

# Replacing characters in a string
sentence = 'Lorem ipsum'
sentence = sentence.replace('s', '5').replace('o', '0')
print(sentence)
