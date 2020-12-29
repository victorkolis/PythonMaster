def zero(*args):
    number = 0
    if len(args) == 0:
        return number
    elif len(args) == 1:
        for character in args:
            if '+' in character:
                return args[0][0] + number
            elif '-' in character:
                return number - args[0][0]
            elif '*' in character:
                return args[0][0] * number
            elif '/' in character:
                return number // args[0][0]


def one(*args):
    number = 1
    if len(args) == 0:
        return number
    elif len(args) == 1:
        for character in args:
            if '+' in character:
                return args[0][0] + number
            elif '-' in character:
                return number - args[0][0]
            elif '*' in character:
                return args[0][0] * number
            elif '/' in character:
                return number // args[0][0]


def two(*args):
    number = 2
    if len(args) == 0:
        return number
    elif len(args) == 1:
        for character in args:
            if '+' in character:
                return args[0][0] + number
            elif '-' in character:
                return number - args[0][0]
            elif '*' in character:
                return args[0][0] * number
            elif '/' in character:
                return number // args[0][0]


def three(*args):
    number = 3
    if len(args) == 0:
        return number
    elif len(args) == 1:
        for character in args:
            if '+' in character:
                return args[0][0] + number
            elif '-' in character:
                return number - args[0][0]
            elif '*' in character:
                return args[0][0] * number
            elif '/' in character:
                return number // args[0][0]


def four(*args):
    number = 4
    if len(args) == 0:
        return number
    elif len(args) == 1:
        for character in args:
            if '+' in character:
                return args[0][0] + number
            elif '-' in character:
                return number - args[0][0]
            elif '*' in character:
                return args[0][0] * number
            elif '/' in character:
                return number // args[0][0]


def five(*args):
    number = 5
    if len(args) == 0:
        return number
    elif len(args) == 1:
        for character in args:
            if '+' in character:
                return args[0][0] + number
            elif '-' in character:
                return number - args[0][0]
            elif '*' in character:
                return args[0][0] * number
            elif '/' in character:
                return number // args[0][0]


def six(*args):
    number = 6
    if len(args) == 0:
        return number
    elif len(args) == 1:
        for character in args:
            if '+' in character:
                return args[0][0] + number
            elif '-' in character:
                return number - args[0][0]
            elif '*' in character:
                return args[0][0] * number
            elif '/' in character:
                return number // args[0][0]


def seven(*args):
    number = 7
    if len(args) == 0:
        return number
    elif len(args) == 1:
        for character in args:
            if '+' in character:
                return args[0][0] + number
            elif '-' in character:
                return number - args[0][0]
            elif '*' in character:
                return args[0][0] * number
            elif '/' in character:
                return number // args[0][0]


def eight(*args):
    number = 8
    if len(args) == 0:
        return number
    elif len(args) == 1:
        for character in args:
            if '+' in character:
                return args[0][0] + number
            elif '-' in character:
                return number - args[0][0]
            elif '*' in character:
                return args[0][0] * number
            elif '/' in character:
                return number // args[0][0]


def nine(*args):
    number = 9
    if len(args) == 0:
        return number
    elif len(args) == 1:
        for character in args:
            if '+' in character:
                return args[0][0] + number
            elif '-' in character:
                return number - args[0][0]
            elif '*' in character:
                return args[0][0] * number
            elif '/' in character:
                return number // args[0][0]


def plus(number): return number, '+'
def minus(number): return number, '-'
def times(number): return number, '*'
def divided_by(number): return number, '/'


print(eight(minus(three())))
