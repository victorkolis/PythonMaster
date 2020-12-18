from tkinter import *

root = Tk()
root.title('Button')


def change_background():
    label.config(text='You clicked me')
    root.config(bg='red')


label = Label(root, text='Hello World')
label.pack()

button1 = Button(root, text='Click Me', command=change_background)
button1.pack()

# Changing the button state
button2 = Button(root, text='Click Me', command=change_background)
button2.pack()
button2['state'] = 'disabled'

root.geometry('350x300')
root.mainloop()
