# Variables are names used to store data in Python

import sys

my_age = 26
my_name = 'Victor Kolis'

print('Hello', my_name)

'''
Multiline comment
'''

# Escape sequences

str_1 = "\"This is a quote\""

'''
Newline: \n
Backslash: \\
Single Quote: \'
Backspace: \b
Tab: \t
'''

# Integer practical maximum size
print(sys.maxsize)

# Float maximum size
print(sys.float_info.max)

# Floats are precise up to 15 digits
f1 = 1.1111111111111111
f2 = 1.1111111111111111
f3 = f1 + f2
print(f3)

# Complex numbers
comp_num1 = 5 + 6j
print(comp_num1)

# Boolean
is_male = True

# type() built-in function & casting
print("Cast 1", type(int(5.4)))
print("Cast 2", type(str(5.4)))
print("Cast 3", type(chr(97)))
print("Cast 4", type(ord('a')))
print("Cast 5", type(float(2)))

# Case sensitive

a = 3
A = 5

num1 = '1'
num2 = '2'
print(f'{num1} + {num2} = ', int(num1) + int(num2))
