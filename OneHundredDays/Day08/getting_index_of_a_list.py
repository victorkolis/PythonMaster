# getting_index_of_a_list.py

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
text = "victor kolis"
text = list(text)


for i in range(len(text)):
    if text[i] == ' ':
        text[i] = -1
    else:
        text[i] = alphabet.index(text[i])
print(text)
