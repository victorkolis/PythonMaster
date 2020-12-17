# prime_number_checker.py

def prime(number_entered):
    is_prime = "?"

    number_entered = abs(number_entered)
    if number_entered > 3 and number_entered % 2 == 0 or number_entered == 1:
        return f"{number_entered} is not a prime number."
    elif number_entered > 3:
        for i in range(3, number_entered):
            if number_entered % i == 0:
                is_prime = f"{number_entered} is not a prime number."
                break
            else:
                is_prime = f"{number_entered} is a prime number."
    else:
        is_prime = f"{number_entered} is a prime number."
        return is_prime
    return is_prime


n = int(input("Check this number: "))
number = prime(number_entered=n)
print(number)
