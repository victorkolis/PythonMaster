from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Check Box')
WIDTH, HEIGHT = '200', '300'
app_title = Label(root, text='CHECK BOX', font=('American typewriter', 20), padx=int(WIDTH)//6)
root.geometry(f'{WIDTH}x{HEIGHT}')
root.resizable(False, False)
app_title.grid(row=0, column=0)
checkbox_var = IntVar()
checkbox_var.set(0)
checkbox = Checkbutton(root, text='Check me', variable=checkbox_var, font=('American typewriter', 20)).\
    grid(row=4, column=0)

button = ttk.Button(root, text='Button')
button.grid()

root.mainloop()
