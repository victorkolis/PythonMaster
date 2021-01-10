#!/usr/local/bin/python3
from math import pi
import sys


def circle(radius):
    return round(pi * int(radius) ** 2, 2)


def help():
    print('''\
            It's necessary inform the circle radius.
            Syntax: {} <radius>'''.format(sys.argv[0]))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(1)
    #   sys.exit(errno.EPERM), errno.EPERM = 1
    elif not sys.argv[1]:
        print('The radius must be a numeric value')

    else:
        try:
            radius_entered = sys.argv[1]
            circle_area = circle(radius_entered)
            print('The area of the circle is {}'.format(circle_area))
        except ValueError:
            print('''This is not a number.''')
        except IndexError:
            pass
