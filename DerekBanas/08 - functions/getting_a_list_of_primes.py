def is_prime(num):
    for _ in range(2, num):
        if num % _ == 0:
            return False
    return True


def get_primes(last_number):
    prime_list = []
    for num in range(2, last_number):
        if is_prime(num):
            prime_list += [num]
    return prime_list


primes_up_to = int(input('Enter a value to get the prime numbers up to it: '))
prime_list_final = get_primes(primes_up_to)

for prime in prime_list_final:
    print(prime)
