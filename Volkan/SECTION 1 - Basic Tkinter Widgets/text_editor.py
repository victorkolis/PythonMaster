from tkinter import *
from tkinter import ttk


def save_content():
    content = text_editor.get(1.0, END)  # 1.0 from the first letter to the end
    print(content)


root = Tk()
root.title('TEXT EDITOR')
WIDTH, HEIGHT = 400, 500
root.geometry(f'{WIDTH}x{HEIGHT}+400+200')
root.resizable(False, False)

text_editor = Text(root, width=25, height=10, font=('American typewriter', 16), wrap=WORD)
text_editor.grid(row=0, column=0, pady=20, padx=60)
text_editor.insert(INSERT, '** text goes here **')
text_editor.focus()

button = ttk.Button(root, text='save', command=save_content).grid(row=3, column=0)

root.mainloop()
