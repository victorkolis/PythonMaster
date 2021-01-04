from animal import Animal
from cat import Cat
from fish import Fish
from bird import Bird

animal = Animal(animal_type='Horse')
animal.breath()
print()

cat = Cat()
cat.name = 'Sophie'
cat.animal_type = 'Cat'
cat.breath()
cat.lick()
print()

fish = Fish()
fish.name = 'Bret'
fish.animal_type = 'Fish'
fish.breath()
fish.swim()
print()

bird = Bird()
bird.name = 'Feathers'
bird.animal_type = 'Bird'
bird.breath()
bird.fly()
print()

bird2 = Bird()
bird2.animal_type = 'Bird'
bird2.breath()
bird2.fly()
print()

bird3 = Bird()
bird3.breath()
bird3.fly()
print()
