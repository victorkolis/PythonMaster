def draw_a_cross(n):
    half = n // 2
    cross = ''
    spacer = ' '
    if n > 2 and n % 2 == 0:
        return 'Centered cross not possible!'
    elif n < 2:
        return 'Not possible to draw cross for grids less than 3x3!'
    else:
        # Cross first part
        n -= 2
        number_of_spaces = 0
        for number_of_spaces in range(half):
            cross += spacer * number_of_spaces
            cross += 'x'
            cross += spacer * n
            cross += 'x'
            cross += spacer * number_of_spaces
            cross += '\n'
            n -= 2

        # Central x
        number_of_spaces += 1
        cross += spacer * number_of_spaces
        cross += 'x'
        cross += spacer * number_of_spaces

        # Cross latter part
        n += 2
        half -= 1
        for number_of_spaces in range(half, -1, -1):
            cross += '\n'
            cross += spacer * number_of_spaces
            cross += 'x'
            cross += spacer * n
            cross += 'x'
            cross += spacer * number_of_spaces
            n += 2

    return cross


print(draw_a_cross(11))
