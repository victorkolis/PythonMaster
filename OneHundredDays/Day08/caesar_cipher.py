# author : Victor Kolis
# caesar_cipher.py

import math

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
shifted_alphabet = list(alphabet)


wanna_continue = 'yes'


while wanna_continue == 'yes' or wanna_continue == 'y':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = math.trunc(float(input("Type the shift number:\n")))
    text = list(text)
    text_as_list = text
    shifted_alphabet = list(alphabet)
    final_text = ""

    # shift the list the amount the user entered
    try:
        if direction == 'encode':
            for index in range(len(alphabet)):
                shifted_alphabet[index - shift] = alphabet[index]
        elif direction == 'decode':
            shift  = -shift 
            for index in range(len(alphabet)):
                shifted_alphabet[index] = alphabet[index + shift]
    except IndexError:
        print("This number is not allowed!")

    # change each item on the list to their original position/index on the unaltered alphabet list
    for index in range(len(text)):
        if text[index] == ' ':
            text[index] = -1
        else:
            text[index] = shifted_alphabet.index(text[index])

    # change each item on the list back to their new position/index on the altered alphabet list
    for index in range(len(text)):
        if text[index] == -1:
            text[index] = ' '
        else:
            text[index] = alphabet[text[index]]

    for letter in text:
        final_text += letter
    
    
    print(final_text)
    wanna_continue = input("Do you wanna continue(y/n)? ")
