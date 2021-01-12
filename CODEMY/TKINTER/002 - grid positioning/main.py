from tkinter import *
from tkinter import Tk


root = Tk()

label_1 = Label(root, text='LEARNING THE GRID SYSTEM')
label_2 = Label(root, text='IN TKINTER')

# Grid positioning is object related
label_1.grid(row=0, column=0)
label_2.grid(row=1, column=1)

root.mainloop()
