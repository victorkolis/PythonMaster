# A simple hello world software

from tkinter import *

# Instantiating/Creating the object
menu_principal = Tk()

# Set title
menu_principal.title("Hello World")

# Define the window dimensions and location
menu_principal.geometry("400x400+500+300")

# Define is resizable or not
menu_principal.resizable(True, False)

# Infinite loop
menu_principal.mainloop()
