from tkinter import *
from tkinter import Tk

# Setting the main window
root = Tk()
root.title('LABELS AND PACK')
root.resizable(False, False)
WIDTH, HEIGHT = 300, 500
root.geometry(f'{WIDTH}x{HEIGHT}+450+200')
root.config(bg='#232323')


def labels():   # Setting the labels

    label_1 = Label(root, text='LABELS AND PACK', bg='#232323', font=('American typewriter', 20), foreground='white')
    label_1.pack()

    label_2 = Label(root, text='WEST ANCHORED LABEL', font=('American typewriter', 10))
    label_2.config(bg='#232323', fg='#ffffff')
    top_padding, bottom_padding = 100, 20
    label_2.pack(pady=(top_padding, bottom_padding), anchor=W)

    label_3 = Label(root, text='IPADY-TAKE-THE-WHOLE-SCREEN LABEL')
    label_3.pack(ipady=10, fill='x')


labels()
root.mainloop()
