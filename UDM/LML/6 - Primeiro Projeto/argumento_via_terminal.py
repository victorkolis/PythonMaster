#!/usr/local/bin/python3
from math import pi
import sys


def circle(radius):
    return round(pi * int(radius) ** 2, 2)


if __name__ == '__main__':
    radius_entered = sys.argv[1]
    circle_area = circle(radius_entered)
    print('The area of the circle is {}'.format(circle_area))
