tree_height = int(input('How tall is the tree: '))

tree_pines = tree_height * 2
space_distance = tree_height - 1
space_distance_final = space_distance

for _ in range(tree_pines):
    if _ % 2 == 0:
        continue
    else:
        pine = ''
        spaces = ''
        for space in range(space_distance):
            spaces += ' '
        for __ in range(_):
            pine += "#"
        print(spaces + pine)
    space_distance -= 1

for _ in range(space_distance_final):
    spaces += ' '
print(spaces + "#")
