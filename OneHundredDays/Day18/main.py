from turtle import Turtle
from turtle import Screen

bert = Turtle()
screen = Screen()
bert.shape("turtle")
bert.color('tomato')


def turtle_moves():
    for _ in range(18):
        bert.forward(200)
        bert.left(100)


turtle_moves()
screen.exitonclick()
