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
print(string.isalpha())  # Alphabetical only
print(string.isalnum()) # Alphabetical or numerical only (spaces and others are not considered)
print(string.isdecimal()) # Numerical only
print(string.isspace()) # Spaces only
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

# ljust() & rjust()
