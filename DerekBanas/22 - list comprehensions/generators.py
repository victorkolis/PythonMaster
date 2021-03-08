#!/usr/bin/env python3

# Get the prime numbers
def is_odd(number):
	for iterator in range(2, number):
		if number % iterator == 0:
			return False
		return True


def odd_generator(number_of_primes_to_get):
	for num in range(2, number_of_primes_to_get):
		if is_odd(num):
			yield num  # yield is what makes this function a generator


# next is used to call the following result of a given generator
prime = odd_generator(50)
print('Prime :', next(prime))
print('Prime :', next(prime))
print('Prime :', next(prime))
print('Prime :', next(prime))
print('Prime :', next(prime))
print('Prime :', next(prime))
