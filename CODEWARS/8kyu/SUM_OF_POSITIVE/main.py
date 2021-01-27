def positive_sum(arr):
    result = 0
    for element in arr:
        if element > 0:
            result += element
    return result


print(positive_sum([1,-2,3,4,5]))
