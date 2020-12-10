names = ['Victor', 'Isaac', 'Vinicius',]
subject = ['You', 'They', 'We']
past_be = ['was', 'were']
action_verb = ['walking.', 'talking.', 'working.', 'coding']

# f strings
print(f'{names[0]} {past_be[0]} {action_verb[3]}.')


# interpolation
print('%s %s %s.' % (names[0], past_be[0], action_verb[3]))

# format() function
print('{} {} {}.'.format(names[0], past_be[0], action_verb[3]))
