from turtle import Turtle
from turtle import Screen
import random

bert = Turtle()
bert.speed(0)

screen = Screen()
screen.colormode(255)


def random_color():
    for _ in range(3):
        r = random.randrange(0, 255)
        g = random.randrange(0, 255)
        b = random.randrange(0, 255)
    color = (r, g, b)
    return color


for _ in range(1, 360):
    bert.color(random_color())
    bert.circle(100)
    bert.left(1)

screen.exitonclick()
