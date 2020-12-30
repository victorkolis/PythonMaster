from turtle import Turtle, Screen
import random

bert = Turtle()
bert.speed(0)
screen = Screen()
screen.colormode(255)

hidden = False


# Binding keystrokes to events
def move_forwards():
    bert.forward(10)


def left():
    bert.left(10)


def right():
    bert.right(10)


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


def hide():
    global hidden
    if not hidden:
        hidden = True
        bert.hideturtle()
    else:
        hidden = False
        bert.showturtle()


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
screen.onkey(hide, "h")

screen.exitonclick()
