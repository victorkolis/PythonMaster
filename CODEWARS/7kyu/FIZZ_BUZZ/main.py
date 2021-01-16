def fizzbuzz(n: int) -> str and int:
    n += 1
    fizzbuzz_list = []
    for number in range(1, n):
        if number % 3 == 0 and number % 5 == 0:
            fizzbuzz_list += ['FizzBuzz']
        elif number % 5 == 0:
            fizzbuzz_list += ['Buzz']
        elif number % 3 == 0:
            fizzbuzz_list += ['Fizz']
        else:
            fizzbuzz_list += [number]
    return fizzbuzz_list
