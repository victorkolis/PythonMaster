from tkinter import *
from tkinter import ttk


class App():

    def __init__(self):

        # Screen display
        self.root = Tk()
        self.root.title('Simple Add Calculator')
        self.root.resizable(False, False)

        # Entry
        self.calculation_display = Entry(self.root, width=35, borderwidth=5)
        self.calculation_display.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        # Style of the buttons/Layout
        self.style = ttk.Style()
        self.style.theme_use('alt')
        self.style.configure('TButton', font=('American typewriter', 50), background='#232323', foreground='white', height=40)
        self.style.map('TButton', background=[('active', '#00ff66')])

        # Buttons
        self.button_1 = ttk.Button(self.root, text='1', width=10, command=self.button_add)
        self.button_2 = ttk.Button(self.root, text='2', width=10, command=self.button_add)
        self.button_3 = ttk.Button(self.root, text='3', width=10, command=self.button_add)
        self.button_4 = ttk.Button(self.root, text='4', width=10, command=self.button_add)
        self.button_5 = ttk.Button(self.root, text='5', width=10, command=self.button_add)
        self.button_6 = ttk.Button(self.root, text='6', width=10, command=self.button_add)
        self.button_7 = ttk.Button(self.root, text='7', width=10, command=self.button_add)
        self.button_8 = ttk.Button(self.root, text='8', width=10, command=self.button_add)
        self.button_9 = ttk.Button(self.root, text='9', width=10, command=self.button_add)
        self.button_0 = ttk.Button(self.root, text='0', width=10, command=self.button_add)

        # Button layout organization
        self.button_7.grid(row=1, column=0, )
        self.button_8.grid(row=1, column=1, )
        self.button_9.grid(row=1, column=2, )

        self.button_4.grid(row=2, column=0, )
        self.button_5.grid(row=2, column=1, )
        self.button_6.grid(row=2, column=2, )

        self.button_1.grid(row=3, column=0, )
        self.button_2.grid(row=3, column=1, )
        self.button_3.grid(row=3, column=2, )
        self.button_0.grid(row=4, column=0, )

        self.root.mainloop()


    def button_add(self):
        return 0


def main():
    App()


main()
