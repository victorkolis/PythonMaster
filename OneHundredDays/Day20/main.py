from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)

snake = Snake()
game_is_on = True
counter = 0
while game_is_on:
    counter += 1
    screen.update()
    time.sleep(0.1)
    snake.move()
    if counter == 20:
        break
