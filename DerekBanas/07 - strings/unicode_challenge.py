# Challenge: Convert the characters into unicode and be able to undo it when needed

# Converting regular upper case string to unicode
text = input("Enter some word: ").upper()
unicode_word = ''

for letter in text:
    unicode_word += str(ord(letter))

print(unicode_word)

# Converting unicode back to letters
for index in range(len(unicode_word) - 1, 2):
    text += chr(int(unicode_word[index] + unicode_word[index + 1]))

print(text)
