# 1. Have user enter their investment amount and expected interest
# 2. Each year their investment will increase by their investment + their investment * the interest
# 3. Print out their earnings after a 10 year period

investment = float(input('Enter your investment: '))
interest_rate = float(input('Enter your interest: ')) * .01

for _ in range(10):
    investment += investment * interest_rate

print('Your investment after 10 years is ${:.2f}'.format(investment))
