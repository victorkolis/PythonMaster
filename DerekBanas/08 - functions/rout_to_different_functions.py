import math


def get_area(shape):
    shape = shape.lower()
    if shape == 'rectangle':
        rectangle_area()
    elif shape == 'circle':
        circle_area()
    else:
        print('Enter a circle or a rectangle')


def rectangle_area():
    length = float(input('Enter the length: '))
    width = float(input('Enter the width: '))
    area = width * length
    print('The area of the rectangle is', area)


def circle_area():
    radius = float(input('Enter the radius: '))
    π = math.pi
    area = round(π * radius ** 2, 2)
    print('The area of the circle is', area)


user_input = input('Enter the shape (circle/rectangle): ')
get_area(user_input)
