def disemvowel(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    new_string = ''
    for letter in string:
        if letter.lower() not in vowels:
            new_string += letter
    return new_string


print(disemvowel('VICTOR'))
