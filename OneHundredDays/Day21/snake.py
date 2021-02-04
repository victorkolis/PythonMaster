from turtle import Turtle


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

        # Snake directions
        self.UP, self.DOWN, self.LEFT, self.RIGHT = 90, 270, 180, 0

    def create_snake(self):
        screen_x_position = 0
        screen_y_position = 0
        for _ in range(3):
            snake = Turtle()
            snake.penup()
            snake.color('white')
            snake.shape('square')
            snake.goto(x=screen_x_position, y=screen_y_position)
            screen_x_position -= 20
            self.segments += [snake]
    

    # Making the snake move forwards automatically
    def move(self):
        for index in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[index - 1].xcor()
            new_y = self.segments[index - 1].ycor()
            self.segments[index].goto(new_x, new_y)
        self.segments[0].forward(20)

    # Controlling the snake
    def up(self):
        if not self.segments[0].heading() == self.DOWN:
            self.segments[0].setheading(self.UP)

    def down(self):
        if not self.segments[0].heading() == self.UP:
            self.segments[0].setheading(self.DOWN)

    def left(self):
        if not self.segments[0].heading() == self.RIGHT:
            self.segments[0].setheading(self.LEFT)

    def right(self):
        if not self.segments[0].heading() == self.LEFT:
            self.segments[0].setheading(self.RIGHT)
