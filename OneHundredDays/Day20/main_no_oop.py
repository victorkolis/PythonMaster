from turtle import Screen
from turtle import Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)


# Creating the snake
SCREEN_X_POSITION = 0
SCREEN_Y_POSITION = 0

segments = []
for _ in range(3):
    snake = Turtle()
    snake.speed(1)
    snake.penup()
    snake.color('white')
    snake.shape('square')
    snake.goto(x=SCREEN_X_POSITION, y=SCREEN_Y_POSITION)
    SCREEN_X_POSITION -= 20
    segments += [snake]


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for index in range(len(segments) - 1, 0, -1):
        new_x = segments[index - 1].xcor()
        new_y = segments[index - 1].ycor()
        segments[index].goto(new_x, new_y)
    segments[0].forward(20)

screen.exitonclick()
