# caesar_cipher.py

import math

alphabet =         ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
shifted_alphabet = list(alphabet)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = math.trunc(abs(float(input("Type the shift number:\n"))))

def encrypt(plain_text):    
    
    for index in range(len(alphabet)):
        shifted_alphabet[index - shift] = alphabet[index]
    

encrypt(plain_text=text)
