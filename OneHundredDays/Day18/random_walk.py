from turtle import Turtle
from turtle import Screen
import random

# Turtle settings
bert = Turtle()
degrees = [90, 180, 90, 180]
true_false = [True, False]
bert.speed(0)
bert.pensize(10)
distance = [50, 100]

# Screen settings
screen = Screen()
screen.colormode(255)


def walk():
    for _ in range(2000):
        color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        bert.pencolor(color)
        boolean = random.choice(true_false)
        if boolean:
            bert.left(random.choice(degrees))

        else:
            bert.right(random.choice(degrees))

        bert.forward(random.choice(distance))


walk()
screen.exitonclick()
