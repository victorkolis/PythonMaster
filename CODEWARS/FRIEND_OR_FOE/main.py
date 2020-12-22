def friend(x):
    y = []
    for name in x:
        if len(name) == 4:
            y += [name]

    return y


print(friend(['Ed', 'Four', 'Ryan', 'Kolis']))
