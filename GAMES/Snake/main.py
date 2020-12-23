from tkinter import *
from PIL import Image, ImageTk


class Snake(Canvas):
    def __init__(self):
        # By standard the canvas's got a border, thus, the highlightthickness = 0
        super().__init__(width=800, height=600, background='black', highlightthickness=0)

        self.snake_positions = [(100, 100), (80, 100), (60, 100)]
        self.apple_position = (200, 100)

        self.load_assets()
        self.create_objects()

    def load_assets(self):
        try:
            self.snake_body_image = Image.open("./assets/snake.png")
            self.snake_body = ImageTk.PhotoImage(self.snake_body_image)

            self.apple_food = Image.open("./assets/apple.png")
            self.apple = ImageTk.PhotoImage(self.apple_food)
        except IOError as error:
            print(error)
            root.destroy()

    def create_objects(self):
        for x_position, y_position in self.snake_positions:
            self.create_image(x_position, y_position, image=self.snake_body, tag='snake')

        self.create_image(*self.apple_position, image=self.apple, tag='food')


# MAIN DISPLAY/WINDOW
root = Tk()
root.title('Snake')
root.resizable(0, 0)

# BOARD
board = Snake()
board.pack()

root.mainloop()
