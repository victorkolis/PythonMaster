def valid_parentheses(characters):
    characters = characters.strip()
    string = ''
    for character in characters:
        if character == '(' or character == ')':
            string += character

    if string == '':
        return True
    elif string[0] == ')':
        return False
    else:
        while string.count('()') > 0:
            string = string.replace('()', '')
        return len(string) == 0


print(valid_parentheses("hi(hi)()"))
