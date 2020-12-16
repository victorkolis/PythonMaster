# Importing a specific module and creating an alias
from decimal import Decimal as D

from decimal import *

sum_number = D(0)
sum_number += D("0.01")
sum_number += D("0.01")
sum_number += D("0.01")
sum_number -= D("0.05")

print(sum_number)

sum_number1 = Decimal(0)
sum_number1 += Decimal("0.0111111111111111111111111")
sum_number1 += Decimal("0.0111111111111111111111111")
print("Sum =", sum_number1)

# Sum = 0E-25
sum_number1 -= Decimal("0.0222222222222222222222222")
print("Sum =", sum_number1)
