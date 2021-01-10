import time


class TerminalColor:
    black = '\u001b[30m'  # \u001b[30m
    red = '\u001b[31m'  # \u001b[31m
    green = '\u001b[32m'  # \u001b[32m
    yellow = '\u001b[33m'  # \u001b[33m
    blue = '\u001b[34m'  # \u001b[34m
    magenta = '\u001b[35m'  # \u001b[35m
    cyan = '\u001b[36m'  # \u001b[36m
    white = '\u001b[37m'  # \u001b[37m


text = 'WELCOME TO THE HACK COMMUNITY'

for letter in text:
    time.sleep(0.5)
    print(TerminalColor.red, letter, end=' ')
