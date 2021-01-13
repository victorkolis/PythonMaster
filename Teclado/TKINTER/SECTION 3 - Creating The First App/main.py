from tkinter import *
from tkinter import ttk


def greet():
    print(f'Hello {user_name.get().title() or "World"}!')


# Creating the window
root = Tk()
root.title('Greeting App')
root.geometry('800x600+200+0')

# Creating the hello world label
label = ttk.Label(root, text='Made By Victor Kolis', padding=(100, 10))
label.pack()

user_name = StringVar()

name_label = ttk.Label(root, text='Enter Your Name Below: ')
name_label.pack()

name_entry = ttk.Entry(root, width=15, textvariable=user_name)
name_entry.focus()
name_entry.pack()

# Creating the greet button
greet_button = ttk.Button(root, text='Greet', command=greet)
greet_button.pack()

# Quit button
quit_button = ttk.Button(root, text='Quit', command=root.destroy)
quit_button.pack()

root.mainloop()
