age = int(input('Enter your age: '))

if not age >= 1 or age > 120:
    print('Invalid age')
elif age == 5:
    print('Go to Kindergarten')
elif 6 <= age <= 17:
    grade = age - 5
    print('Go to grade ', str(grade))
elif age > 17:
    print('Go to college')
else:
    print('Too young for school')
