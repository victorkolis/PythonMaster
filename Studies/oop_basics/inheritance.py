# Inheritance

# Upper level class


class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'I am {self.name} and I am {self.age} years old.')


class Cat(Pet):
    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age

    def speak(self):
        print('Meow')


class Dog(Pet):
    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age

    def speak(self):
        print('Bark')


p = Pet('Mr Furs', 7)
p.show()

c = Cat('Further', 12)
c.show()
c.speak()

d = Dog('Mylo', 5)
d.show()
d.speak()
