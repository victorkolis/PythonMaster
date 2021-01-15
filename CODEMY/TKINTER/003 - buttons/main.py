from tkinter import *
from tkinter import ttk


class App:
    def __init__(self):

        # Window setup
        self.root = Tk()
        self.root.title('BUTTONS')
        WIDTH, HEIGHT = 300, 500
        INITIAL_X_POSITION, INITIAL_Y_POSITION = 450, 200
        self.root.geometry(f'{WIDTH}x{HEIGHT}+{INITIAL_X_POSITION}+{INITIAL_Y_POSITION}')
        self.root.resizable(0, 0)
        self.style = ttk.Style()

        # Layout
        self.button_1 = ttk.Button(self.root, text='click me', command=self.show_me_pi)
        self.style.theme_use('alt')
        self.style.configure('TButton', font=('American typewriter', 14), background='#232323', foreground='white')
        self.style.map('TButton',
                       background=[('active', '#232323')]
                       )
        self.button_1.bind('<Enter>', self.on_enter)
        self.button_1.pack()

        self.button_2 = ttk.Button(self.root, text='click me', state='disabled')
        self.button_2.pack()
        self.root.mainloop()

    def show_me_pi(self):
        py_label = Label(self.root, text='3.14159', font=('American typewriter', 20))
        py_label.pack()

    def on_enter(self, e):

        return e


app_runner = App()
