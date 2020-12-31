text_file = open('main.txt', 'r')
print(text_file.read())


# a, append, add to the end of the file without deleting or overwriting it
# r, read the file.
# w, write to the file
# x, create a new file if it's not already created

# Reading line-by-line
text_file = open('main.txt', 'r')
print(text_file.readline())

text_file = open('main.txt', 'r')
for line in text_file:
    if line == '\n':
        continue
    else:
        print(line, end='')

text_file.close()
