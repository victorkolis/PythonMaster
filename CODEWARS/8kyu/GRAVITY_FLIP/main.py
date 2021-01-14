def flip(d, a):
    if d == 'R':
        a.sort()
        return a
    else:
        a.sort()
        a.reverse()
        return a


print(flip('L', [3, 2, 1, 2]))
