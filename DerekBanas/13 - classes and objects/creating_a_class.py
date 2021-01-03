class Dog:
    def __init__(self, name='', weight=0, height=0):
        self.name = name
        self.weight = weight
        self.height = height

    def bark(self):
        print('{} the dog barks'.format(self.name))

    def run(self):
        print('{} the dog runs'.format(self.name))

    def eat(self):
        print('{} the dog eats'.format(self.name))


def main():
    dog_1 = Dog('Ribs', weight=20, height=30)
    dog_1.bark()


main()
