from tkinter import *
from tkinter import ttk


class App:
    def __init__(self):

        # Screen setup
        self.root = Tk()
        self.root.title('INPUT FIELDS')
        WIDTH, HEIGHT = 300, 500
        self.root.geometry(f'{WIDTH}x{HEIGHT}+450+200')
        self.root.resizable(False, False)

        # Layout
        # Entry field
        self.input_1 = Entry(self.root, show='*', width=30, bg='#0055ff', fg='#fff', borderwidth=5)
        self.input_1.pack()

        # Buttons style
        self.style = ttk.Style()
        self.style.theme_use('alt')
        self.style.configure('TButton', font=('American typewriter', 14), background='#232323', foreground='#fff')
        self.style.map('TButton', background=[('active', '#434343')])

        # Buttons
        self.button_1 = ttk.Button(self.root, text='click me', command=self.show_my_data_entry, width=10)
        self.button_1.pack()

        self.root.mainloop()

    def show_my_data_entry(self):
        data_entered = Label(self.root, text=self.input_1.get())
        data_entered.pack()


def main():
    App()


main()
