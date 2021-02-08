#!/usr/bin/env python3

import string


def move_ten(st):
    alphabet = string.ascii_lowercase    
    new_alpha = []
    for element in st:
        new_alpha += [alphabet[alphabet.index(element) + 10 if alphabet.index(element) + 10 < 25 else alphabet.index(element) - 16]]

    return ''.join(new_alpha)


print(move_ten('victor'))

