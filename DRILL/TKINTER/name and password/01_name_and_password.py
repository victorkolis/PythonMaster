from tkinter import *
from tkinter import ttk


def print_info():
    name = name_entry.get()
    password = password_entry.get()
    print(name, f'\n{password}')
    root.destroy()


# Root configuration
root = Tk()
root.title('Name & Password')
root.resizable(False, False)
WIDTH, HEIGHT = 300, 400
root.geometry(f'{WIDTH}x{HEIGHT}+450+200')
screen_center = 24

# Title Label
title_label = Label(root, text='NAME & PASSWORD', padx=WIDTH/screen_center, font=('American typewriter', 24))
title_label.grid(row=0, column=0, padx=WIDTH/screen_center)

# Entries configuration
name_entry = Entry(root)
name_entry.insert(0, 'Enter your full name')
name_entry.focus()
name_entry.grid(row=1, column=0, pady=20)

password_entry = Entry(root)
password_entry.config(show='*')
password_entry.grid(row=2, column=0, pady=1)

# Button
submit = ttk.Button(root, text='submit', command=print_info)
submit.grid(row=3, column=0, pady=2)

root.mainloop()
