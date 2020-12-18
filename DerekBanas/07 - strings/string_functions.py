text = 'This is just an experimental text. No reason to panic.'

print('text.capitalize() =', text.capitalize())
print('text.upper() =', text.upper())
print('text.lower() =', text.lower())

# String to list
text_list = text.split()
print('text.split() = ', text_list)

# List of every single character
text_character_list = list(text)
print('Every single character list', text_character_list)

# List to string using a space " " as a delimiter
print('" ".join(text_list)  = ', " ".join(text_list))

# Find out how many times a given set of string occurs in a string
print('text.count(" an")', text.count(" an"))  # Space is used here so 'an' occurrences show not up such as "p 'an'  ic"

# Find out how many letters happen/there are in a word
print('"Supercalafajalistickespeealadojus".count("") - 1 =', "Supercalafajalistickespeealadojus".count("") - 1)
print('"Supercalafajalistickespeealadojus".count("a") =', "Supercalafajalistickespeealadojus".count("a"))
