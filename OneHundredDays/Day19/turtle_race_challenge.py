from turtle import Turtle
from turtle import Screen
import random

is_race_on = False
screen = Screen()
WIDTH, HEIGHT = 800, 600
screen.setup(width=WIDTH, height=HEIGHT)
chosen_turtle = screen.textinput(title='Turtles', prompt='Choose your ninja').lower()


def finish_liner():
    finish_line = Turtle(visible=False)
    finish_line.color('green')
    finish_line.penup()
    finish_line.goto(250, 300)
    finish_line.pendown()
    finish_line.pensize(20)
    finish_line.right(90)
    finish_line.forward(600)


def bet_liner():
    bet_line = Turtle(visible=False)
    bet_line.color('red')
    bet_line.penup()
    bet_line.goto(-100, 300)
    bet_line.pendown()
    bet_line.pensize(5)
    bet_line.right(90)
    bet_line.forward(600)


leonardo = Turtle(shape='turtle')
leonardo.color('red')
leonardo.penup()
leonardo.goto(-300, 250)

raphael = Turtle(shape='turtle')
raphael.color('blue')
raphael.penup()
raphael.goto(-300, 100)

michelangelo = Turtle(shape='turtle')
michelangelo.color('orange')
michelangelo.penup()
michelangelo.goto(-300, -50)

donatello = Turtle(shape='turtle')
donatello.color('purple')
donatello.penup()
donatello.goto(-300, -200)

finish_liner()
bet_liner()

if chosen_turtle:
    is_race_on = True

while is_race_on:
    leonardo.forward(random.randrange(0, 2))
    raphael.forward(random.randrange(0, 2))
    michelangelo.forward(random.randrange(0, 2))
    donatello.forward(random.randrange(0, 2))
    if leonardo.xcor() > 250 or raphael.xcor() > 250 or michelangelo.xcor() > 250 or donatello.xcor() > 250:

        if leonardo.xcor() > 250:
            winner = leonardo.color()
            leonardo.forward(20)
        elif raphael.xcor() > 250:
            winner = raphael.color()
            raphael.forward(20)
        elif michelangelo.xcor() > 250:
            winner = michelangelo.color()
            michelangelo.forward(20)
        elif donatello.xcor() > 250:
            winner = donatello.color()
            donatello.forward(20)

        if chosen_turtle == winner[0]:
            print('You win!')
        else:
            print(f'You lose! The {winner[0]} is the winner.')
        break

screen.exitonclick()
