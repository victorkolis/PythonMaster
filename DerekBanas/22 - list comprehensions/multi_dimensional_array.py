#!/usr/bin/env python3

multi_list = [[1, 2, 3],
			  [4, 5, 6],
			  [7, 8, 9]]


# Getting a column
print([column[1] for column in multi_list])

# Getting the diagonal
print([multi_list[x][x] for x in range(len(multi_list))])
