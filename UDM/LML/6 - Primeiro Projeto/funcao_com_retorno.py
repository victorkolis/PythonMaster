#!/usr/local/bin/python3
from math import pi


def circle(radius):
    return round(pi * radius ** 2, 2)


if __name__ == '__main__':
    radius_entered = float(input('Enter the radius value: '))
    circle_area = circle(radius_entered)
    print('The area of the circle is {}'.format(circle_area))
