try:
    num1, operator, num2 = input("Enter calculation: ").split()
    num1 = int(num1)
    num2 = int(num2)
    
except ValueError:
    request = 'invalid'
    operator = ''

sum = 0
request = ''

if operator == '*':
    sum = num1 * num2

elif operator == '/':
    sum = num1 / num2

elif operator == '+':
    sum = num1 + num2

elif operator == '-':
    sum = num1 - num2

elif operator == 'ˆ':
    sum = num1 ** num2

else:
    print('Invalid request')
    request = 'invalid'

if request == 'invalid':
    pass
else:
    print('{} {} {} = {}'.format(num1, operator, num2, sum))
