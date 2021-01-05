from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def delete():
    mbox = messagebox.askquestion('Delete', 'Are you sure?', icon='warning')
    if mbox == 'yes':
        print('Deleted')
    else:
        print('Not deleted')


def info():
    messagebox.showinfo('Success', 'by Code Future Invent')
    mbox = messagebox.askyesnocancel('Delete', 'Save document?')

    if mbox:
        print('Saved')
        root.destroy()

    elif not mbox:
        print('Document not saved')
        root.destroy()
    else:
        print('Canceled')


root = Tk()
root.title('MESSAGEBOX')
WIDTH, HEIGHT = 400, 300
SCREEN_CENTER = 3.5
root.geometry(f'{WIDTH}x{HEIGHT}+450+200')
root.resizable(False, False)

label_title = Label(root, text='MESSAGEBOX', font=('American typewriter', 20))\
    .grid(row=0, column=0, pady=20)

button_1 = ttk.Button(root, text='Delete', command=delete).grid(row=2, column=0, pady=2)
button_2 = ttk.Button(root, text='Info', command=info).grid(row=2, column=1, pady=2)

root.mainloop()
