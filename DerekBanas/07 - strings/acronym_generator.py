words = input('Enter the words you want to acronym: ').title()

words_list = words.split()

acronym = ''
for _ in range(len(words_list)):
    acronym += words_list[_][0]

print(acronym)
print(words)
