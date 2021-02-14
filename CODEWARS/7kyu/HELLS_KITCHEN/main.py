#!/usr/bin/env python3

# Transform all the words from gordon such as Word -> WORD!!!!

def gordon(text):
    text = text.upper()
    text = text.replace('A', '@')
    text = text.replace('E', '*').replace('I', '*').replace('O', '*').replace('U', '*')
    
    return text.replace(' ', '!!!! ') + '!!!!'


print(gordon('What feck damn cake'))

