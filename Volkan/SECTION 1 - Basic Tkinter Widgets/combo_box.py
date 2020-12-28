import mailbox
from tkinter import *
from tkinter import ttk


def get_combobox():
    combo_box_value = f'{months.get()} {numbers.get()}'
    print(combo_box_value)


root = Tk()
root.title('COMBO BOX')
root.resizable(False, False)
WIDTH, HEIGHT = 400, 500
root.geometry(f'{WIDTH}x{HEIGHT}+450+200')

label_title = Label(root, text='COMBO BOX', font=('American typewriter', 20)).grid(row=0, column=0, padx=WIDTH / 16)

# Combobox
months = StringVar()
numbers = StringVar()
number_list = list(range(11))

combo_box1 = ttk.Combobox(root, textvariable=months,
                          values=('Jan', 'Feb', 'Mar', 'Apr', 'May'), state='readonly').grid(row=1, column=0)

combo_box2 = ttk.Combobox(root, textvariable=numbers,
                          values=number_list, state='readonly').grid(row=2, column=0)

submit_button = ttk.Button(root, text='submit', command=get_combobox).grid(row=3, column=0)

root.mainloop()
