from tkinter import *
from tkinter import ttk


def callback():
    print('You are', gender.get())


root = Tk()
root.title('Radio Button')
WIDTH, HEIGHT = 200, 300
root.geometry(f'{WIDTH}x{HEIGHT}')
root.resizable(False, False)

title_label = Label(root, text='Radio Button', font=('American typewriter', 28))
title_label.grid(row=2, column=0, padx=WIDTH//24)

button = ttk.Button(root, text='Enter', command=callback)
button.grid(row=4, column=0)


# Radio Button
gender = StringVar()
male = ttk.Radiobutton(root, text='male', value='male', var=gender).grid(row=5, column=0)
female = ttk.Radiobutton(root, text='female', value='female', var=gender).grid(row=6, column=0)

root.mainloop()
