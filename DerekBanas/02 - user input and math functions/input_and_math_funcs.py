# Accepting input
name = input('What is your name? ')
print('Hello', name)


# Accepting more than one value input
num1, num2 = input('Enter 2 numbers: ').split()
num1 = int(num1)
num2 = int(num2)

# Format function
print("{} + {} = {}".format(num1, num2, num1 + num2))
print("{} - {} = {}".format(num1, num2, num1 - num2))
print("{} * {} = {}".format(num1, num2, num1 * num2))
print("{} / {} = {}".format(num1, num2, num1 / num2))
print("{} // {} = {}".format(num1, num2, num1 // num2))
print("{} % {} = {}".format(num1, num2, num1 % num2))
