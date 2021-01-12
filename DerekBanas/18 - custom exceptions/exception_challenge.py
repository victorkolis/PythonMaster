file = open('error.txt')

try:
    file_name = input('Please enter the file name: ')
    file = open(file_name, 'r')
    print(file.read())
except FileNotFoundError as file_not_found:
    print(file.read())
    print(file_not_found.args)

finally:
    file.close()
