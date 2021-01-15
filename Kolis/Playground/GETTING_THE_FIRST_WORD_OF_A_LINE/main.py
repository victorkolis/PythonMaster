try:
    adjectives = []
    text = open('text.txt', 'r')
    new_text = open('new_text.txt', 'w')
    for line in text.readlines():
        adjectives += [line.split()[0]]

    adjectives.sort()
    new_text.write('\n'.join(adjectives))

except FileExistsError:
    print('File does not exist')

else:
    text.close()
