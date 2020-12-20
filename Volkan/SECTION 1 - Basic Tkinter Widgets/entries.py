from tkinter import *
from tkinter import ttk

# Creating the root/window object
root = Tk()
root.title('Name And Password')


# Getting info collected from entries via a button
def callback():
    name_value = str(entry1.get())
    password_value = str(entry2.get())

    print(f'{name_value} {password_value}')


# entry1 - name
entry1 = ttk.Entry(root, width=30)
entry1.insert(0, "Please enter your name")
entry1.pack()

# entry2 - password
entry2 = Entry(root, width=30)
entry2.config(show='*')
entry2.pack()

# entry3
entry3 = ttk.Entry(root, width=30)
entry3.insert(0, 'This is a read only')
entry3.state(['readonly'])
entry3.pack()

# entry4 - states only exists within ttk module
entry4 = ttk.Entry(root, width=10)
entry4.insert(0, 'Disabled')
entry4.state(['disabled'])
entry4.pack()


# button
button = Button(root)
button.config(text='submit', command='callback')
button.pack()

# Settings
root.resizable(False, False)
root.geometry('400x600')
root.mainloop()
