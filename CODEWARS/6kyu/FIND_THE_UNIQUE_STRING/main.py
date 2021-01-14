def find_unique(arr):
    for index in range(len(arr)):
        if arr[index] == '':
            arr[index] = ' '
        for letter in arr[0]:
            if not letter.lower() in arr[index].lower():
                return arr[index]


print(find_unique(['Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a']))
