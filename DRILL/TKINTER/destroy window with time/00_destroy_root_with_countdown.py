import time
from tkinter import *
from tkinter import ttk


def plus_fifteen_secs():
    global seconds
    seconds += 15


def minus_fifteen_secs():
    global seconds
    seconds -= 15


# Root setup
root = Tk()
root.title('COUNTDOWN DESTROYER')
WIDTH, HEIGHT = 400, 500
SCREEN_CENTER = 6
root.geometry(f'{WIDTH}x{HEIGHT}+450+200')
root.resizable(False, False)


text = StringVar()
seconds = 9

while seconds >= 0:
    add_button = ttk.Button(root, text='15+', command=plus_fifteen_secs)
    add_button.grid(row=1, column=0, pady=10)

    subtract_button = ttk.Button(root, text='15-', command=minus_fifteen_secs)
    subtract_button.grid(row=2, column=0, pady=1)

    if seconds < 10:
        text.set(f'This window will shut down in 0{seconds} seconds')
    else:
        text.set(f'This window will shut down in {seconds} seconds')
    label = Label(root, textvariable=text, wraplength='300', font=('American typewriter', 24))
    label.grid(row=0, column=0, padx=WIDTH/SCREEN_CENTER)

    if seconds >= 0:
        time.sleep(1)
        seconds -= 1
        root.update()
