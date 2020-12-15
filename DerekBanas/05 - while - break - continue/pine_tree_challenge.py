tree_height = int(input('How tall is the tree: '))

tree_pines = tree_height * 2
space_distance = tree_height - 1
space_distance_trunk = space_distance
spaces = ''

# Get the odd numbers
for pine_amount in range(tree_pines):
    if pine_amount % 2 == 0:
        continue
    else:
        pine = ''
        spaces = ''

        # Get the spaces
        for space in range(space_distance):
            spaces += ' '

        # Get the pines
        for _ in range(pine_amount):
            pine += "#"
        print(spaces + pine)
    space_distance -= 1

# Get the trunk
for pine_amount in range(space_distance_trunk):
    spaces += ' '
print(spaces + "#")
