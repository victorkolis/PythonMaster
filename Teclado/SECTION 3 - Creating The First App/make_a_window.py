from tkinter import *

# Root/Window Setup
root = Tk()
root.title('')
root.geometry('600x400+200+500')

rectangle_1 = Label(root, text='Rectangle 1', bg='green', fg='white')
rectangle_1.pack(side='left', ipadx=10, ipady=10, fill='x', expand=True)

rectangle_2 = Label(root, text='Rectangle 2', bg='red', fg='white')
rectangle_2.pack(ipadx=10, ipady=10, fill='y', expand=True)

"""
fill: y, x, both
expand: True, makes the widget take up the entire space
reserved for it on the root/window, however, respecting
other widgets surrounding it.

Using expand without the fill would make the widget still 
consider both in fill, but it would not indeed fill the given spaces.
"""

root.mainloop()
