from tkinter import Tk
from tkinter import ttk
import tkinter

# Define and set up main/root window
root = Tk()
WIDTH, HEIGHT = 300, 500
X_POSITION, Y_POSITION = 450, 200
BG_COLOR = '#232323'

root.geometry(f'{WIDTH}x{HEIGHT}+{X_POSITION}+{Y_POSITION}')
root.config(bg=BG_COLOR)
root.title('BUTTON AND GRID')
root.resizable(0, 0)

# Define layout
name_button = ttk.Button(root, text='name')
name_button.grid(row=0, column=0)

time_button = ttk.Button(root, text='time')
time_button.grid(row=0, column=1)


place_button = ttk.Button(root, text='white')
place_button.grid(row=0, column=2, padx=10, ipady=5)


day_button = tkinter.Button(root, text='day')
day_button.grid(row=1, column=0, columnspan=3, sticky='WE')

root.mainloop()
