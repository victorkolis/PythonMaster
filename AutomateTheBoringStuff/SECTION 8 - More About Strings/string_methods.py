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

