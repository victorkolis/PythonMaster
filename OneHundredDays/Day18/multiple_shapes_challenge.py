from turtle import Turtle
from turtle import Screen

bert = Turtle()
screen = Screen()


def draw_shapes():
    bert.penup()
    bert.left(90)
    bert.forward(100)
    bert.right(90)
    bert.left(180)
    bert.forward(100)
    bert.pendown()
    bert.left(180)

    # Triangle
    for _ in range(3):
        bert.forward(100)
        bert.right(120)

    # Square
    for _ in range(4):
        bert.color('red')
        bert.forward(100)
        bert.right(90)

    # Pentagon
    for _ in range(5):
        bert.color('blue')
        bert.forward(100)
        bert.right(72)

    # Hexagon
    for _ in range(6):
        bert.color('green')
        bert.forward(100)
        bert.right(60)

    # Heptagon
    for _ in range(7):
        bert.color('red')
        bert.forward(100)
        bert.right(51.4)

    # Octagon
    for _ in range(8):
        bert.color('gray')
        bert.forward(100)
        bert.right(45)


draw_shapes()
screen.exitonclick()
