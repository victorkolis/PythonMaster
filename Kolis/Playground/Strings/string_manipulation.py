"""

There is plenty of ways of manipulate strings in Python. Be it by the
built-in modules or its libraries. But the string manipulation can be
more customizable and more specific than that.

"""

# Simple letter replacement
name = 'ABCDEFG'
name = name.replace('E', '3')
print(name)

# Chained replace()
name = name.replace('B', 'HIJK').replace('F', '8')
print(name)

"""

If you want to get more specific with the replacement, there is a way
around for the string methods.

"""

# Replacing specific indexes
""" Convert the string to a list """
name = list(name)

""" Looping over the newly created list in order to access its indexes """ 
for letter_index in range(len(name)):
    if letter_index % 2 == 0:
        name[letter_index] = '*'

""" Converting the list back into a string"""        
name = ''.join(name)
print(name)
