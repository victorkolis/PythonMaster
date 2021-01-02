import os

with open('my_file.txt', mode='w', encoding='utf-16') as my_file:
    my_file.write('This has been written with Python script.')

with open('my_file.txt', encoding='utf-16') as my_file:
    print(my_file.read())

print(my_file.closed)

print(my_file.name)
print(my_file.mode)

try:
    for _ in range(20):
        os.mkdir('Q1W2E3R4')
        os.chdir('Q1W2E3R4')
except FileExistsError:
    pass

print(os.getcwd())

os.chdir('Q1W2E3R4/Q1W2E3R4/Q1W2E3R4/Q1W2E3R4')
print(os.getcwd())
