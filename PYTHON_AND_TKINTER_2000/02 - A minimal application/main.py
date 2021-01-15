#!/usr/local/bin/python3
from tkinter import *
from tkinter import ttk


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets(self)

    @staticmethod
    def create_widgets(self):
        self.quit_button = ttk.Button(self, text='Quit', command=self.quit)
        self.quit_button.grid()


app = Application()
app.master.title('Sample Application')
app.mainloop()
