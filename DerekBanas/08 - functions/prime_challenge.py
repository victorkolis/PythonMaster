def is_prime(num):
    counter = 0
    for _ in range(2, num - 1):
        if num % _ == 0:
            counter += 1
            if counter >= 2:
                print('Not Prime')
    if counter <= 1:
        print('Prime')


print('Welcome to the Prime checker')
is_prime(int(input('Enter a number: ')))
