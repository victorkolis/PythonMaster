"""
An isogram is a word that has no repeating letters, consecutive or non-consecutive.
Implement a function that determines whether a string that contains only letters is an isogram.
Assume the empty string is an isogram. Ignore letter case.
"""


def is_isogram(string):



words = ['Dermatoglyphics', 'isogram', 'aba', 'moOse', 'isIsogram', '']

for word in words:
    if is_isogram(word) is not None:
        print(is_isogram(word))
