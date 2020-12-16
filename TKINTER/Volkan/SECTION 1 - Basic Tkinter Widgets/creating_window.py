from tkinter import *
from tkinter import ttk

# The window object is normally named root
root = Tk()

# Set the size of the window
root.geometry("400x100")

# Creating buttons
click_me_button1 = Button(root, text='Click Me')
click_me_button2 = ttk.Button(root, text='Click Me')

# Make buttons visible
click_me_button1.pack()
click_me_button2.pack()

# This is the main loop which makes the window updates and keep it up
root.mainloop()
