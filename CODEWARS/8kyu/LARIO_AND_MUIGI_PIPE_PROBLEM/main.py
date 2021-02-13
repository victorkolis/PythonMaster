#!/usr/bin/env python3

# Complete a given integer list [1, 3, 6] -> [1, 2, 3, 4, 5, 6]
def pipe_fix(nums):
	return [x for x in range(nums[0], nums[len(nums) - 1] + 1)]


print(pipe_fix([-10, 10]))
