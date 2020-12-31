import string


def find_missing_letter(chars):
    chars_set = set()
    lowercase_alphabet = set()
    uppercase_alphabet = set()

    if chars[0].islower():
        comparison_index = string.ascii_lowercase.find(chars[0])
        for letter in chars:
            chars_set.add(letter)
        for index in range(1, len(chars) + 1):
            lowercase_alphabet.add(string.ascii_lowercase[comparison_index + index])
        missing_letter = str(lowercase_alphabet.difference(chars))[2]
    else:
        comparison_index = string.ascii_uppercase.find(chars[0])
        for letter in chars:
            chars_set.add(letter)
        for index in range(1, len(chars) + 1):
            uppercase_alphabet.add(string.ascii_uppercase[comparison_index + index])
        missing_letter = str(uppercase_alphabet.difference(chars))[2]
    return missing_letter


print(find_missing_letter(['O', 'Q', 'R', 'S']))
