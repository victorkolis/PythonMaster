from tkinter import *
from tkinter import Tk

root = Tk()
root.title('WINDOWS BASICS')
root.iconbitmap('thinking.ico')

WIDTH, HEIGHT = 300, 500
root.geometry(f'{WIDTH}x{HEIGHT}+450+200')
root.resizable(False, False)
root.config(bg='blue')

# Top level window
top_1 = Toplevel()
top_1.title('TOP LEVEL WINDOW')
top_1.resizable(False, False)
top_1.config(bg='green')


root.mainloop()
