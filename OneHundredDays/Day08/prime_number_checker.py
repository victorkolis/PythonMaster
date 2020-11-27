# prime_number_checker.py

def prime(number):
    isPrime = "?"
    
    number = abs(number)    
    if number > 3 and number % 2 == 0  or number == 1:
        return f"{number} is not a prime number."
    elif number > 3:
        for i in range(3, number):
            if number % i == 0:
                isPrime = f"{number} is not a prime number."
                break
            else:
                isPrime = f"{number} is a prime number."
    else:
        isPrime = f"{number} is a prime number."
        return isPrime
    return isPrime    

n = int(input("Check this number: "))
number = prime(number = n)
print(number)
