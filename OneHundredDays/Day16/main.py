# import my_module
# from turtle import Turtle, Screen
#
#
# print(my_module.variable)
#
# # Constructing an object
# bert = Turtle()
#
# # Methods
# bert.shape('turtle')
# bert.color('chocolate4')
# bert.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()


table.add_column('Names', ['Victor', 'Vinicius', 'Isaac'])
table.add_column('Age', ['26', '26', '2'])
table.align = 'r'
print(table)
