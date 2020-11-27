# shitfing_a_list.py

import math

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# make a newly declared list have the same size as a given list
shifted_alphabet = list(alphabet)

shift = math.trunc(abs(float(input("List shift: "))))
for index in range(len(alphabet)):
    shifted_alphabet[index - shift] = alphabet[index]

print(shifted_alphabet)
