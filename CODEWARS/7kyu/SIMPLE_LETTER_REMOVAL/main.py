def solve(string, k):
    string = list(string)
    original_string = list(string)
    original_string.sort()

    for _ in range(k):
        try:
            string.remove(original_string[0])
            original_string.remove(original_string[0])
        except IndexError:
            pass

    return ''.join(string)


print(solve('abracadabra', 18))
