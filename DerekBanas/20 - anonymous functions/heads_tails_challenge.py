# Toss the heads and tails a certain amount and the output the number of times each their lot.

import random

heads_tails = {'Heads': 0,
               'Tails': 0}

for toss in range(100):
    random_key = random.choice(list(heads_tails.keys()))
    if random_key == 'Heads':
        heads_tails['Heads'] += 1
    else:
        heads_tails['Tails'] += 1


for index in range(len(heads_tails)):
    print('{}: {}'.format(list(heads_tails.keys())[index], list(heads_tails.values())[index]))
