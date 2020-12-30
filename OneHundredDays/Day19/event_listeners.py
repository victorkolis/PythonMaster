from turtle import Turtle, Screen
import random

bert = Turtle()
bert.speed(0)
screen = Screen()
screen.colormode(255)


# Binding keystrokes to events
def move_forwards():
    bert.forward(10)


def left():
    bert.setheading(180)


def right():
    bert.setheading(0)


def up():
    bert.setheading(90)


def down():
    bert.setheading(270)


def clear():
    bert.clear()


def penup():
    bert.penup()


def pendown():
    bert.pendown()


def color():
    bert.color((random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)))


def restart():
    bert.reset()


screen.listen()
screen.onkey(key="space", fun=move_forwards)
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(clear, "c")
screen.onkey(penup, "u")
screen.onkey(pendown, "d")
screen.onkey(color, "q")
screen.onkey(restart, "r")

screen.exitonclick()
