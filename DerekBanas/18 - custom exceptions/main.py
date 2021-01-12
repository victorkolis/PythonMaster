class NameViolation(Exception):
    def __init__(self, *args):
        Exception.__init__(self, *args)


try:
    name = input('Name: ')
    if any(char.isdigit() for char in name):
        raise NameViolation
except NameViolation:
    print('NameViolation: Names must only have alphabetic characters')
