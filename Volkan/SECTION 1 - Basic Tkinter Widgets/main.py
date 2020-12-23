from tkinter import *
from tkinter import ttk


def callback():
    print(entry_name.get())
    print(entry_password.get())


# Window setup
# root setup
root = Tk()
WIDTH, HEIGHT = '500', '600'
root.geometry(f'{WIDTH}x{HEIGHT}+200+500')
root.title('GRID LAYOUT')
root.resizable(0, 0)

# Software Title
title_lbl = Label(root, text='Scala', font=('American typewriter', 40), padx=int(WIDTH)//10)
title_lbl.grid(row=1, column=1)
title_lbl.config()


# Labels setup

name_lbl = Label(root, text='Enter your name', font=('American typewriter', 15))
name_lbl.grid(row=2, column=0, sticky=W)

password_lbl = Label(root, text='Enter your password', font=('American typewriter', 15))
password_lbl.grid(row=3, column=0)

# Entries setup
# entry_name setup (NAME)
entry_name = ttk.Entry(root, width=30)
entry_name.insert(0, 'Enter your name')
entry_name.focus()
entry_name.grid(row=2, column=1)

# entry_password setup (PASSWORD)
entry_password = ttk.Entry(root, width=30)
entry_password.config(show='*')
entry_password.grid(row=3, column=1)

# Buttons setup
# button1 setup
button1 = ttk.Button(root, text='Click me', command=callback)
button1.grid(row=4, column=1, sticky=E+W, pady=5)

# Checkbox
checkbox_var = IntVar()
checkbox_var.set(0)
checkbox = Checkbutton(root, text='Check me', variable=checkbox_var,
                       font=('American typewriter', 20)).grid(sticky=W)

root.mainloop()
