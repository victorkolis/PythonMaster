# Inheritance

# Upper level class


class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'I am {self.name} and I am {self.age} years old.')

    def speak(self):
        print("I don't know what to say.")


class Cat(Pet):
    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print('Meow')

    def show(self):
        print(f'I am {self.name} and I am {self.age} years old and I am {self.color}.')


class Dog(Pet):
    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age

    def speak(self):
        print('Bark')


p = Pet('Mr Furs', 7)
p.show()
p.speak()

c = Cat('Further', 12, 'White')
c.show()
c.speak()

d = Dog('Mylo', 5)
d.show()
d.speak()
