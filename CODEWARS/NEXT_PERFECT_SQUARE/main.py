import math


def find_next_square(sq):
    initial_sq = sq
    sq = math.sqrt(sq)
    if '.0' in str(sq):
        sq = round(sq)
        sq += sq + 1 + initial_sq

        return sq
    else:
        return -1


print(find_next_square(144))
