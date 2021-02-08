#!/usr/bin/env python3

# Sort a given list. At times it might have string and ints

def db_sort(text):
    
    string = []
    numbers = []
    
    for element in text:
        try:
            if element.isprintable():
                string += [element]
        except AttributeError:
            numbers += [element]

    
    return sorted(numbers) + sorted(string)
print(db_sort(["Banana", "Orange", "Apple", "Mango", 0, 2, 2]))

