# how_many_characters.py

import pprint

message = 'The quieter you become, the more you are able to hear.'.lower()
count = {}

for letter in message:
    count.setdefault(letter, 0)
    count[letter] = count[letter] + 1

# Std print
print(count,end='\n\n')

# Neater way of printing
pprint.pprint(count)

# If some return is needed/wanted
pprint_return = pprint.pformat(count)
print(pprint_return)
