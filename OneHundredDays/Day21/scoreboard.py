from turtle import Turtle

ALIGNMENT = 'center'
SCORE_FONT = ('Courier', 20, 'normal')
GAMEOVER_FONT = ('Courier', 100, 'normal')



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
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=SCORE_FONT)
        
    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align=ALIGNMENT, font=GAMEOVER_FONT,)

    def increase_score(self):
        self.score += 1
        self.update_score()
