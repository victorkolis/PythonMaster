def iq_test(numbers):
    # Turn the string of numbers into a list of strings
    numbers = numbers.split()

    # Converting every single string into an integer
    numbers = [int(string) for string in numbers]

    # The counters bellow serve to know the majority of type of number
    even_counter = 0
    odd_counter = 0

    # Checking numbers to see whether the majority is odd or even
    # If there is only one even only one value is going to be stored into the even_index
    # If there is more than one even value then we know we need the odd one
    for index in range(len(numbers)):
        if numbers[index] % 2 == 0:
            even_counter += 1
            even_index = numbers.index(numbers[index])
        else:
            odd_counter += 1
            odd_index = numbers.index(numbers[index])

    # The counters finally get to be used. And if the majority is odd then we need the even number
    # And vice-versa
    # Since the challenge emphasized the fact the indexes should not work with zeroes, thus, the + 1
    if even_counter < odd_counter:
        return even_index + 1
    else:
        return odd_index + 1


number_list = '1 1 3 4 7 9'
print(iq_test(number_list))
