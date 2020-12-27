import mailbox
from tkinter import *
from tkinter import ttk

root = Tk()
root.title('COMBO BOX')
root.resizable(False, False)
WIDTH, HEIGHT = 400, 500
root.geometry(f'{WIDTH}x{HEIGHT}+450+200')


label_title = Label(root, text='COMBO BOX', font=('American typewriter', 20)).grid(row=0, column=0, padx=WIDTH/16)

months = StringVar()
combo_box = ttk.Combobox(root, textvariable=months).grid(row=1, column=0)

root.mainloop()
