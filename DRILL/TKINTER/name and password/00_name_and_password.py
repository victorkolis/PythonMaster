from tkinter import *
from tkinter import ttk

# Setting the window up
root = Tk()
root.title('User and Password 01')
root.geometry('300x400')
root.resizable(0, 0)

name_label = ttk.Label(root, text='Enter your name:', width=30)
name_label.pack()

name_entry = ttk.Entry(root, width=30)
name_entry.focus()
name_entry.insert(0, 'e.g Victor Kolis')
name_entry.pack()

password_label = ttk.Label(root, text='Enter your password:', width=30)
password_label.pack()

password_entry = ttk.Entry(root)
password_entry.config(show='*', width=30)
password_entry.pack()

root.mainloop()
