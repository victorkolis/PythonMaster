from turtle import Turtle
from turtle import Screen

screen = Screen()
WIDTH, HEIGHT = 800, 600
screen.setup(width=WIDTH, height=HEIGHT)

SCREEN_Y_POSITION = 250
colors = ['red', 'blue', 'orange', 'purple']
for index in range(4):
    bert = Turtle(shape='turtle')
    bert.penup()
    bert.color(colors[index])
    bert.penup()
    SCREEN_X_POSITION = -300
    bert.goto(SCREEN_X_POSITION, SCREEN_Y_POSITION)
    SCREEN_Y_POSITION -= 150


screen.exitonclick()
