class Dog:
    num_of_dogs = 0

    def __init__(self, name='Unknown'):
        self.name = name
        Dog.num_of_dogs += 1

    @staticmethod
    def get_num_of_dogs():
        print('There are {} dogs currently.'.format(Dog.num_of_dogs))


def main():
    Dog(name='Pete')
    Dog(name='Klaus')
    Dog(name='Mythic')
    Dog(name='Mr. Barks')
    Dog.get_num_of_dogs()


main()
