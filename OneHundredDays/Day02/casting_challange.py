# This software objective is to get a two digit number int and add the two digits

#01 - Better for readability and variable manipulation
two_digit_number = input("Type a two digit number: ")
num1 = int(two_digit_number[0])
num2 = int(two_digit_number[1])

print(num1 + num2)

#02 - Not so good for readability
#two_digit_number = input("Type a two digit number: ")
# print(two_digit_number[0] + two_digit_number[1])