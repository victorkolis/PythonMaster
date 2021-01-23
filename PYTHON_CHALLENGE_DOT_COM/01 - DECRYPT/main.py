import string

text = """
g fmnc wms bgblr rpylqjyrc gr zw fylb. 
rfyrq ufyr amknsrcpq ypc dmp. 
bmgle gr gl zw fylb gq glcddgagclr ylb  rfyr'q ufw rfgq rcvr gq qm jmle. 
sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. 
lmu ynnjw ml rfc spj."""

alphabet = string.ascii_lowercase

new_text = list(text)

for index, letter in enumerate(text):
    if letter.isalpha():
        letter_index = alphabet.index(letter) - 24
        new_text[index] = alphabet[letter_index]

new_text = ''.join(new_text)

print(new_text)


# K -> M = 1
# O -> Q = 1
# E -> G = 1

