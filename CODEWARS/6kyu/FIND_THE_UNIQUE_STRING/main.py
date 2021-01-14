def find_unique(arr):

    # If the length of the first element is equal to one
    if len(arr[0]) == 1:
        # And that element is found only once in the array list
        if arr.count(arr[0]) == 1:
            return arr[0]
    for index in range(len(arr)):
        if arr[index] == '':
            arr[index] = ' '
        for letter in arr[0]:
            if not letter.lower() in arr[index].lower():
                return arr[index]


print(find_unique(['f', 'a']))
