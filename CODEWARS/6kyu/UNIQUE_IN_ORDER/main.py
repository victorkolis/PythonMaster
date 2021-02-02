#!/usr/bin/env python3

#unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
#unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
#unique_in_order([1,2,2,3,3])       == [1,2,3]


def unique_in_order(iterable):
	if len(iterable) == 1:
		return [iterable]
	elif len(iterable) == 2:
		unique = set()
		for element in iterable:
			unique.add(element)
		return list(unique)
	unique = []
	for index in range(len(iterable)):
		try:
			if iterable[index] != iterable[index + 1]:
				unique += [iterable[index]]
		except IndexError:
			pass
	try:
		if iterable[len(iterable) - 1] != unique[len(unique) - 1]:
			unique += [iterable[len(iterable) - 1]]
	except:
		pass
	return unique
			
			
print(unique_in_order('AA'))

# SOLUTION BY kmeshu09

#def unique_in_order(iterable):
#	result = []
#	prev = None
#	for char in iterable[0:]:
#		if char != prev:
#			result.append(char)
#			prev = char
#	return result
