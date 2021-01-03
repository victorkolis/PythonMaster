class Square:
    def __init__(self, height=0, width=0):
        self.height = height
        self.width = width

    @property  # Getter
    def height(self):
        print('Retrieving the height')
        return self.__height

    @height.setter  # Setter
    def height(self, value):
        if type(value) == (type(0)):
            self.__height = value
        else:
            print("You've tried to enter a value other than numbers so the height is now set to 0.")
            self.__height = 0

    @property  # Getter
    def width(self):
        print('Retrieving the width')
        return self.__width

    @width.setter  # Setter
    def width(self, value):
        if type(value) == (type(0)):
            self.__width = value
        else:
            print("You've tried to enter a value other than numbers so the width is now set to 0.")
            self.__width = 0


def main():
    square = Square(width=100, height=20)
    print(square.height)
    print(square.width)
    square.height = 'a'
    square.width = 'b'
    print(square.height)
    print(square.width)


main()
