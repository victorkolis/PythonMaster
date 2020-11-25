# fizz_buzz_challenge.py
# This software objective is to replace the divisible numbers of -
# 5 and 3, if a given number is divisible by both then the software -
# should print "FizzBuzz", if by 3 only then "Fizz" and if by 5 only then "Buzz"

for fizz_buzz_number_catcher in range(1, 100):
    if fizz_buzz_number_catcher % 3 == 0 and fizz_buzz_number_catcher % 5 == 0:
        print("FizzBuzz")
    elif fizz_buzz_number_catcher % 3 == 0:
        print("Fizz")
    elif fizz_buzz_number_catcher % 5 == 0:
        print("Buzz")
    else:
        print(fizz_buzz_number_catcher)
