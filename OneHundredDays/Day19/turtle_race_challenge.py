from turtle import Turtle
from turtle import Screen

screen = Screen()
WIDTH, HEIGHT = 800, 600
screen.setup(width=WIDTH, height=HEIGHT)
chosen_turtle = screen.textinput(title='Turtles', prompt='Choose your ninja')

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

screen.exitonclick()
