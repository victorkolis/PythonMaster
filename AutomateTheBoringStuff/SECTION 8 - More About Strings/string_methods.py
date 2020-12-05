# string_methods.py

# Strings are immutable, which means it's not possible to modify them in place
string = 'I am immutable'
string.upper()
print(string)

# In this case a reassignment is needed
string = string.upper()
print(string)

# islower() and isupper() - boolean
isStringLower = string.islower()
isStringUpper = string.isupper()
print(isStringLower)
print(isStringUpper)
''' If the character contained in the string being tested
does not have a alphabetical type either the upper or lower methods will return
False '''

string = '2, %'
isStringLower = string.islower()
isStringUpper = string.isupper()
print(isStringLower)
print(isStringUpper)

# Chaining methods
string = 'abc'
string = string.upper().isupper()
print(string)

# More on the 'is' methods
string = 'VictorKolis26MarriedComputerScientist'
# Alphabetical only
print(string.isalpha())

# Alphabetical or numerical only (spaces and others are not considered)
print(string.isalnum())

# Numerical only
print(string.isdecimal())

# Spaces only
print(string.isspace())

# Titles only: 'This Is A Title Like String'
print(string.istitle())

# Checking on indexes
string = '1 A% Ab'
print(string[1].isspace())
print(string[0].isdecimal())
print(string[5].istitle())

# startswith() & endswith()
string = string.startswith('1')
print(string)

string = 'Victor Kolis'
string = string.endswith('B')
print(string)

# join()
animals = ['cats', 'rats', 'tigers', 'rhinoceros']
string = ', '.join(animals)
print(string)

# split()
list_of_words = 'This is going to become a list of words'
list_of_words = list_of_words.split()
print(list_of_words)
''' The split method can have other spliting arguments passed in the paramether. '''

# split(some other argument)
list_of_words = 'This is going to become a list of words'
list_of_words = list_of_words.split('o')
print(list_of_words)

# ljust() & rjust() - inserts a given amount of characters to the right or left of a string
''' The way it works is: if a given string is 5 characters long:
e.g.:

string = 'hello'
string = string.rjust(10, '*')
print(string)

>>> *****hello

the 'string' plus the given amount of characters are
concatenated to make that string(value) a 10 character long string

no second argument automatically pushes spaces
'''

string = 'hi'
string = string.ljust(4, '*').rjust(6, '*') # can be chained or individual
print(string)

# center()
string = 'Kolis'
string = string.center(15, '=')
print(string)


# strip()
string = '     Strip     '
string = string.strip() # removes spaces on either side
print(string)

# lstrip, rstrip - remove spaces on a given side l-left r-right

# striping given letters words from a string on either side not in the middle
string = 'SpamSpamSpamSpamSpamSpamSpamPlastic Spam BottleSpamSpamSpamSpamSpamSpamSpam'
string = string.strip('Spam')
print(string)


# replace
string = 'Victor Kolis'
string = string.replace('o', '0').replace('i', '1').replace('s', '5')
print(string)
