#!/usr/bin/env python3

# Calculate the amount of floors visited [5, 2, 8] -> 9
def elevator_distance(arr: list) -> int:
	floors_visited = 0
	
	for index in range(len(arr)):
		try:
			floors_visited += abs(arr[index] - arr[index + 1])
		except:
			pass
	
		
	return floors_visited
		
		
print(elevator_distance([5, 2, 8]))
