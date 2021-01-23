import random

# Assigning lambdas to variables is not a good practice according to PEP 8: E731

# Simple addition operation
sum1 = lambda x, y: x + y
print('Sum :', sum1(4, 5))


# Ternary
can_play = lambda is_able: True if is_able == 'y' else False
print('Can play?', can_play('y'))

# List
to_the_power = [lambda x: x ** 2,
                lambda x: x ** 3,
                lambda x: x ** 4,]

for power in to_the_power:
    print(power(3))


# Dictionary
synonyms = {'Gripe': lambda: print('Whine'),
            'Stash': lambda: print('Put away'),
            'Thwart': lambda: print('Prevent, upset, foil')
            }

synonyms['Gripe']()

# Random
word = random.choice(list(synonyms.keys()))
synonyms[word]()
