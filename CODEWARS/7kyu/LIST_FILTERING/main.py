#!/usr/bin/env python3

# Remove any string that might occur/be in the list/array

def filter_list(l):
	return [x for x in l if isinstance(x, int)]


print(filter_list([1,2,'a','b']))
