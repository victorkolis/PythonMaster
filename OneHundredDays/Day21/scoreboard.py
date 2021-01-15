from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 20, 'normal')



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()
