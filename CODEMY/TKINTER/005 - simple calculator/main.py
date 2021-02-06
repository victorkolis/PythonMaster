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


        # Buttons
        self.button_1 = Button(self.root, text='1', padx=40, pady=20, command=lambda: self.button_click(1))
        self.button_2 = Button(self.root, text='2', padx=40, pady=20, command=lambda: self.button_click(2))
        self.button_3 = Button(self.root, text='3', padx=40, pady=20, command=lambda: self.button_click(3))
        self.button_4 = Button(self.root, text='4', padx=40, pady=20, command=lambda: self.button_click(4))
        self.button_5 = Button(self.root, text='5', padx=40, pady=20, command=lambda: self.button_click(5))
        self.button_6 = Button(self.root, text='6', padx=40, pady=20, command=lambda: self.button_click(6))
        self.button_7 = Button(self.root, text='7', padx=40, pady=20, command=lambda: self.button_click(7))
        self.button_8 = Button(self.root, text='8', padx=40, pady=20, command=lambda: self.button_click(8))
        self.button_9 = Button(self.root, text='9', padx=40, pady=20, command=lambda: self.button_click(9))
        self.button_0 = Button(self.root, text='0', padx=40, pady=20, command=lambda: self.button_click(0))
        self.button_add = Button(self.root, text='+', padx=40, pady=20, command=lambda: self.button_click())
        self.button_equal = Button(self.root, text='=', padx=99, pady=20, command=lambda: self.button_click())
        self.button_clear = Button(self.root, text='CE', padx=95, pady=20, command=lambda: self.button_click())
        

        # Button layout organization
        self.button_7.grid(row=1, column=0)
        self.button_8.grid(row=1, column=1)
        self.button_9.grid(row=1, column=2)

        self.button_4.grid(row=2, column=0)
        self.button_5.grid(row=2, column=1)
        self.button_6.grid(row=2, column=2)

        self.button_1.grid(row=3, column=0)
        self.button_2.grid(row=3, column=1)
        self.button_3.grid(row=3, column=2)
        self.button_0.grid(row=4, column=0)
        
        self.button_add.grid(row=5, column=0)
        self.button_equal.grid(row=5, column=1, columnspan=2)
        self.button_clear.grid(row=4, column=1, columnspan=2)

        self.root.mainloop()


    def button_click(self):
        self.calculation_display.delete(0, END)
        self.calculation_display.insert(0, number)
        return 0


def main():
    App()


main()
