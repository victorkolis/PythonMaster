import random


class TermColor:
    def __init__(self):
        self.black = '\u001b[30m'
        self.red = '\u001b[31m'
        self.green = '\u001b[32m'
        self.yellow = '\u001b[33m'  # Might look brownish depending on the terminal color
        self.blue = '\u001b[34m'
        self.magenta = '\u001b[35m'
        self.cyan = '\u001b[36m'
        self.white = '\u001b[37m'
        self.colors = [self.red, self.green, self.yellow, self.blue, self.magenta, self.cyan]
        self.random_color = random.choice(self.colors)
        self.reset_color = '\u001b[37m'
