age = int(input('What is your age?\n'))

can_vote = '' if age >= 18 else "'t"
print('You can{} vote'.format(can_vote))
