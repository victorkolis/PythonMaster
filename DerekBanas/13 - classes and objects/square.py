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

    def get_area(self):
        return self.width * self.height


def main():
    print('Welcome to the Square Area Calculator program')
    square = Square()
    square.height = int(input('Enter the square height: '))
    square.width = int(input('Enter the square width: '))
    print(square.get_area())


main()
