from tkinter import *
from tkinter import ttk


def callback():
    if checkbox_var.get() == 1:
        print('You have checked me!')


root = Tk()
root.title('Check Box')
WIDTH, HEIGHT = '200', '300'
app_title = Label(root, text='CHECK BOX', font=('American typewriter', 20), padx=int(WIDTH)//6)
root.geometry(f'{WIDTH}x{HEIGHT}')
root.resizable(False, False)
app_title.grid(row=0, column=0)

# Creating a checkbox
checkbox_var = IntVar()
checkbox_var.set(0)  # 0 unchecked, 1 checked
checkbox = Checkbutton(root, text='Check me', variable=checkbox_var, font=('American typewriter', 20)).\
    grid(row=4, column=0)

button = ttk.Button(root, text='Button')
button.config(command=callback)
button.grid()

root.mainloop()
