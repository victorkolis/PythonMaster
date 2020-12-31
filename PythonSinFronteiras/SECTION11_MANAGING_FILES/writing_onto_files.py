# This program writes some information to a given text file 'main.txt'

text_file = open('main.txt', 'a')
text_file.write('This line was added later with\na Python script.')
text_file.close()

read_file = open('main.txt', 'r')
print(read_file.read())

# Rewriting/overwriting a file
rewrite = open('rewrite_me.txt', 'w')
rewrite.write('This text has been rewritten')
