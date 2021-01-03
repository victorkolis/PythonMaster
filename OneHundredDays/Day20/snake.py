from turtle import Turtle


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        screen_x_position = 0
        screen_y_position = 0
        for _ in range(3):
            snake = Turtle()
            snake.speed(1)
            snake.penup()
            snake.color('white')
            snake.shape('square')
            snake.goto(x=screen_x_position, y=screen_y_position)
            screen_x_position -= 20
            self.segments += [snake]

    def move(self):
        for index in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[index - 1].xcor()
            new_y = self.segments[index - 1].ycor()
            self.segments[index].goto(new_x, new_y)
        self.segments[0].forward(20)