def plus_minus(num1, num2):
    return num1 + num2, num1 - num2


first_num = 144
second_num = 70
plus, minus = plus_minus(first_num, second_num)
print(f'{first_num} + {second_num} =', plus)
print(f'{first_num} - {second_num} =', minus)
