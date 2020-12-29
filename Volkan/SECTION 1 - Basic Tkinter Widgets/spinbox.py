from tkinter import *
from tkinter import ttk


def callback():
    print(year.get())


# IMPORTANT NOTE
# Spinbox is only available in tkinter and not in ttk

root = Tk()
root.title('SPIN BOX')
WIDTH, HEIGHT = 400, 500
SCREEN_CENTER = 2.5
root.geometry(f'{WIDTH}x{HEIGHT}+450+200')
root.resizable(False, False)

label_title = Label(root, text='SPINBOX', font=('American typewriter',  30)).grid(row=0, column=0)

year = StringVar()
spinbox = Spinbox(root, from_=1920, to=2020, textvariable=year, state='readonly').grid(row=1, column=0)

button = ttk.Button(root, text='submit', command=callback()).grid(row=2, column=0, padx=WIDTH/SCREEN_CENTER, pady=10)

root.mainloop()
