from tkinter import *
# The config method works as a sort of CSS for the tkinter objects

# Creating and setting the window object
root = Tk()
root.resizable(False, False)
root.config(bg='green')

# Setting window size and title
root.geometry("400x500")
root.title("USING LABELS")

# Creating labels
label_1 = Label(root, text='THIS IS A LABEL')
label_2 = Label(root, text='THIS IS A LABEL FOR BREAK DEMONSTRATION PURPOSES ONLY AND NOTHING MORE.')

# Text alignment
label_1.config(justify=RIGHT)
label_2.config(justify=LEFT)

# Delimiting the break-line points
label_1.config(wraplength='40')
label_2.config(wraplength='150')

# label['text'] = 'This is a way of changing it but not the most appropriate'
# The best way is via the config() method
label_1.config(text='This is the best way of changing a label')

# Set the font  and background color
label_1.config(font='Georgia', fg='white')
label_1.config(bg='green')

# Making labels visible
label_1.pack()
label_2.pack()

root.mainloop()
