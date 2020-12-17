from turtle import Turtle
from turtle import Screen

bert = Turtle()
screen = Screen()


def bert_makes_a_square():
    for _ in range(2):
        bert.left(180)
        bert.forward(50)

    for _ in range(2):
        bert.left(90)
        bert.forward(50)
        bert.left(90)
        bert.forward(100)

    for _ in range(4):
        bert.forward(100)
        bert.left(90)


bert_makes_a_square()
screen.exitonclick()
