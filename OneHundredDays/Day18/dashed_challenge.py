from turtle import Turtle
from turtle import Screen

bert = Turtle()
screen = Screen()


def bert_walks():
    for _ in range(10):
        bert.forward(10)
        bert.penup()
        bert.forward(10)
        bert.pendown()


bert_walks()
screen.exitonclick()
