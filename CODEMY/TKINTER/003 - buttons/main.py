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

        # Layout
        # Icon
        icon = Image('photo', file='icon.gif')
        self.root.iconphoto(True, icon)

        # Buttons style
        self.style = ttk.Style()
        self.style.theme_use('alt')
        self.style.configure('TButton', font=('American typewriter', 14), background='#232323', foreground='white')
        self.style.map('TButton',
                       background=[('active', '#00aa00'), ('disabled', '#f0f0f0')])

        # Buttons
        self.button_1 = ttk.Button(self.root, text='show me π', command=self.show_me_pi)
        self.button_1.pack()

        self.button_2 = ttk.Button(self.root, text='disabled', state='disabled')
        self.button_2.pack()

        self.root.mainloop()

    def show_me_pi(self):
        py_label = Label(self.root, text='3.14159', font=('American typewriter', 20))
        py_label.pack()


app_runner = App()
