from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        random_x_axis = random.randrange(-270, 270)
        random_y_axis = random.randrange(-270, 270)
        self.goto(random_x_axis, random_y_axis)
        color = ['tomato', 'white', 'yellow']
        self.color(random.choice(color))
