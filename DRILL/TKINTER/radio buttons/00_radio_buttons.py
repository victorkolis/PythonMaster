from tkinter import *
from tkinter import ttk


root = Tk()
root.title('Radio Buttons')
WIDTH, HEIGHT = 300, 400
SCREEN_CENTER = 6
root.geometry(f'{WIDTH}x{HEIGHT}+450+200')
root.resizable(False, False)

# Question label
question = Label(root, text='What is the U.S.A\'s current currency?', font=('American typewriter', 20),
                 wraplength='200').grid(row=0, column=0, padx=WIDTH/SCREEN_CENTER, sticky=N)

# Radio button
answer = StringVar()

right_answer = Radiobutton(root, text='Dollar', value='dollar', var=answer)\
    .grid(row=1, column=0, pady=2, padx=10, sticky=W)
answer_1 = Radiobutton(root, text='Real', value='real', var=answer)\
    .grid(row=2, column=0, pady=2, padx=10, sticky=W)
answer_2 = Radiobutton(root, text='Peso', value='peso', var=answer)\
    .grid(row=3, column=0, pady=2, padx=10, sticky=W)
answer_3 = Radiobutton(root, text='Euro', value='euro', var=answer)\
    .grid(row=4, column=0, pady=2, padx=10, sticky=W)

root.mainloop()
