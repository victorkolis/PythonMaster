# Object Oriented Programming in Python


class Dog:
    # __init__ it instantiates the object right when it is created
    # In other words, the constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Methods = actions = verbs
    def bark(self):
        print('bark! bark!')

    def pee(self):
        return 'Peeing...'

    def get_name(self):
        return self.name

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age


# Instantiating an object
d1 = Dog("Mr. Furs", 12)
d1.bark()

d2 = Dog("Barker", 3)

print(d1.pee())
print(type(d1))
print(d2.get_name())
print(d2.get_age())

# Resetting the age via a method
d2.set_age(40)
print(d2.get_name())
print(d2.get_age())
